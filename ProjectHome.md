2. 6. 2010 - **First release 0.1.1**

After quite some time in production and some bugs squashed It's time for a release.
This release features more stability and proper file organization, it is also considered production quality code.

Features:
  * python-openid 2.x.x support
  * [SimpleRegistration](SimpleRegistration.md), [Pape](Pape.md), [AttributeExchange](AttributeExchange.md) extension support
  * English, French, Slovenian locale

Documentation is in wiki, a good start is [Installation](Installation.md)

This is basicly a fork of [django-openid](http://code.google.com/p/django-openid/), before the rewrite/move to github.

django-openid-consumer aims to do only one thing, simple OpenID auth (with all the extension s python-openid supports) for comments on blogs and similar. It **doesen't** aim to provide any further integration (like for example tighter integration with auth) with Django.