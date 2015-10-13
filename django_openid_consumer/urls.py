from django.conf.urls import url, patterns

urlpatterns = patterns('',
    url(r'^$', 'django_openid_consumer.views.begin'),
    url(r'^complete/$', 'django_openid_consumer.views.complete'),
    url(r'^signout/$', 'django_openid_consumer.views.signout'),
)
