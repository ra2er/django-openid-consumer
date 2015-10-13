# Why aren't those included ? #

Because of plugability. With removing the templates django-openid-consumer is one step closer to being plugable.


### openid\_failure.html ###
```
{% load i18n %}
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<head>
<title>{% trans "OpenID failed" %}</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
</head>

<body>
<h1>{% trans "OpenID failed" %}:</h1>

<p>{{ message|escape }}</p>
</body>
</html>
```

### openid\_signin.html ###
```
{% load i18n %}
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<head>
<title>{% trans "Sign in with your OpenID" %}</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
</head>

<body>
<h1>{% trans "Sign in with your OpenID" %}</h1>

<form action="{{ action }}" method="post">
<p><input class="openid" type="text" name="openid_url"> <input type="submit" value="{% trans "Sign in" %}"></p>
</form>
</body>
</html>
```