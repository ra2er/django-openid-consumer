**This extension/functionality requires python-openid 2.1.0 or newer.**

## What is Attribute Exchange? ##
> OpenID Attribute Exchange is an OpenID service extension for exchanging identity  information between endpoints. Messages for retrieval and storage of identity information are provided.

## How to get it working? ##
Example:
```
OPENID_AX = [{"type_uri": "homepage", "count": 1, "required": False, "alias": "homepage"}, {"type_uri": "fullname", "count":1 , "required": False, "alias": "fullname"}]
```

So basicly, a list of dictionaries with keys:
  * type\_uri  (str)
  * count  (int)
  * required  (bool)
  * alias  (str)

For an explanation on why and how to use this fields, look at the [specs](http://openid.net/specs/openid-attribute-exchange-1_0.html).