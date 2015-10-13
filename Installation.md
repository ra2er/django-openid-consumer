# Dependencies #

  * python-openid (2.x.x) **NOTE**: 2.0.0 Doesen't support ax and pape extensions
  * Django (1.x)
  * Only tested with python 2.6

# Installation #
  1. Install django-openid-consumer:
    * With pip: ` pip install django-openid-consumer `
    * From tarball:
      1. Download the [latest release](http://code.google.com/p/django-openid-consumer/downloads/list)
      1. Unpack: ` tar xvf django-openid-consumer-*.*.tar.gz `
      1. Run: ` cd django-openid-consumer-*.* && python setup.py install `
    * From subversion:
      1. Get the latest source: ` svn checkout http://django-openid-consumer.googlecode.com/svn/trunk/ django-openid-consumer `
      1. Run: ` cd django-openid-consumer && python setup.py install `
  1. Put ` django_openid_consumer ` in your **INSTALLED\_APPS** setting.
  1. Add ` django_openid_consumer.middleware.OpenIDMiddleware ` to your list of **MIDDLEWARE\_CLASSES**, somewhere after the ` django.contrib.sessions.middleware.SessionMiddleware `
  1. Sync the database: ` python manage.py syncdb `
  1. Add the following views to your url configuration:
```
(r'^openid/', include('django_openid_consumer.urls')),
```
  1. Create templates, for reference look at ExampleTemplates