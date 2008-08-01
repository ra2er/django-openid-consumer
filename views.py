from django.http import HttpResponse, HttpResponseRedirect, get_host
from django.shortcuts import render_to_response as render
from django.template import RequestContext
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

import md5, re, time, urllib

import openid   
if openid.__version__ < '2.0.0':
    raise ImportError, 'You need python-openid 2.0.0 or newer'
elif openid.__version__ < '2.1.0':
    from openid.sreg import SRegRequest
else: 
    from openid.extensions.sreg import SRegRequest

from openid.consumer.consumer import Consumer, \
    SUCCESS, CANCEL, FAILURE, SETUP_NEEDED
from openid.consumer.discover import DiscoveryFailure
from yadis import xri

from util import OpenID, DjangoOpenIDStore, from_openid_response
from middleware import OpenIDMiddleware

from django.utils.html import escape

def get_url_host(request):
    if request.is_secure():
        protocol = 'https'
    else:
        protocol = 'http'
    host = escape(get_host(request))
    return '%s://%s' % (protocol, host)

def get_full_url(request):
    return get_url_host(request) + request.get_full_path()

next_url_re = re.compile('^/[-\w/]+$')

def is_valid_next_url(next):
    # When we allow this:
    #   /openid/?next=/welcome/
    # For security reasons we want to restrict the next= bit to being a local 
    # path, not a complete URL.
    return bool(next_url_re.match(next))

def begin(request, sreg=None, extension_args=None, redirect_to=None, 
        on_failure=None):
    
    on_failure = on_failure or default_on_failure
    
    extension_args = extension_args or {}
    if sreg:
        extension_args['sreg.optional'] = sreg
    trust_root = getattr(
        settings, 'OPENID_TRUST_ROOT', get_url_host(request) + '/'
    )
    redirect_to = redirect_to or getattr(
        settings, 'OPENID_REDIRECT_TO',
        # If not explicitly set, assume current URL with complete/ appended
        get_full_url(request).split('?')[0] + 'complete/'
    )
    # In case they were lazy...
    if not redirect_to.startswith('http://'):
        redirect_to =  get_url_host(request) + redirect_to
    
    if request.GET.get('next') and is_valid_next_url(request.GET['next']):
        if '?' in redirect_to:
            join = '&'
        else:
            join = '?'
        redirect_to += join + urllib.urlencode({
            'next': request.GET['next']
        })
    
    user_url = request.REQUEST.get('openid_url', None)
    if not user_url:
        request_path = request.path
        if request.GET.get('next'):
            request_path += '?' + urllib.urlencode({
                'next': request.GET['next']
            })
        
        return render('openid_signin.html', {
            'action': request_path,
        })
    
    if xri.identifierScheme(user_url) == 'XRI' and getattr(
        settings, 'OPENID_DISALLOW_INAMES', False
        ):
        return on_failure(request, _('i-names are not supported'))
    
    consumer = Consumer(request.session, DjangoOpenIDStore())
    try:
        auth_request = consumer.begin(user_url)
    except DiscoveryFailure:
        return on_failure(request, _('The OpenID was invalid'))
    
    # Add extension args (for things like simple registration)
    for name, value in extension_args.items():
        namespace, key = name.split('.', 1)
        if namespace == 'sreg':
            s = SRegRequest()
            for v in value.split(','):
                s.requestField(field_name=v)
            auth_request.addExtension(s)

    redirect_url = auth_request.redirectURL(trust_root, redirect_to)
    return HttpResponseRedirect(redirect_url)

def complete(request, on_success=None, on_failure=None):
    on_success = on_success or default_on_success
    on_failure = on_failure or default_on_failure
    
    consumer = Consumer(request.session, DjangoOpenIDStore())
    # JanRain library raises a warning if passed unicode objects as the keys, 
    # so we convert to bytestrings before passing to the library
    query_dict = dict([
        (k.encode('utf8'), v.encode('utf8')) for k, v in request.GET.items()
    ])

    url = get_url_host(request) + request.path
    openid_response = consumer.complete(query_dict, url)
    
    if openid_response.status == SUCCESS:
        return on_success(request, openid_response.identity_url, openid_response)
    elif openid_response.status == CANCEL:
        return on_failure(request, _('The request was cancelled'))
    elif openid_response.status == FAILURE:
        return on_failure(request, openid_response.message)
    elif openid_response.status == SETUP_NEEDED:
        return on_failure(request, _('Setup needed'))
    else:
        assert False, "Bad openid status: %s" % openid_response.status

def default_on_success(request, identity_url, openid_response):
    if 'openids' not in request.session.keys():
        request.session['openids'] = []
    
    # Eliminate any duplicates
    request.session['openids'] = [
        o for o in request.session['openids'] if o.openid != identity_url
    ]
    request.session['openids'].append(from_openid_response(openid_response))
    
    # Set up request.openids and request.openid, reusing middleware logic
    OpenIDMiddleware().process_request(request)
    
    next = request.GET.get('next', '').strip()
    if not next or not is_valid_next_url(next):
        next = getattr(settings, 'OPENID_REDIRECT_NEXT', '/')
    
    return HttpResponseRedirect(next)

def default_on_failure(request, message):
    return render('openid_failure.html', {
        'message': message
    })

def signout(request):
    request.session['openids'] = []
    next = request.GET.get('next', '/')
    if not is_valid_next_url(next):
        next = '/'
    return HttpResponseRedirect(next)
