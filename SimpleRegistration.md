Simple registration (or sreg) is an extension to the OpenID specification that allows you to request extra details about a user from their OpenID provider. It is frequently used to pre-populate registration forms with information such as the user’s name, e-mail address or date of birth.

Be aware that not all OpenID providers support sreg, and there is no guarantee that the information you have requested will be returned. Simple registration should be used as a convenience for your users rather than as a required step in your authentication process.

Available simple registration fields are:
  * nickname
  * email
  * fullname
  * dob (Date of Birth)
  * gender
  * postcode
  * country
  * language
  * timezone.
Full details are available in the [spec](http://openid.net/specs/openid-simple-registration-extension-1_0.html).

To request this information, add an OPENID\_SREG setting to your settings. Example:
```
OPENID_SREG = {"requred": "nickname, email", "optional":"postcode, country", "policy_url": "http://example.com/policy"}
```
"required" and "optional" keys are self explanatory. "policy\_url" key should contain a link to a page where user can read why the requested data will be used.

Any simple registration fields that are returned will be available in a dictionary as the sreg property of the OpenID object:
```
def example_sreg(request):
    if request.openid and request.openid.sreg.has_key('email'):
        return HttpResponse("Your e-mail address is: %s" % escape(
            request.openid.sreg['email']
        ))
    else:
        return HttpResponse("No e-mail address")
```

This documentation was copied from http://django-openid.googlecode.com/svn/trunk/openid.html