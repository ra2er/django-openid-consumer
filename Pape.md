**This extension/functionality requires python-openid 2.1.0 or newer.**

## What is pape ? ##
openid.net said:
> This extension to the OpenID Authentication protocol provides a mechanism by which a  Relying Party can request that particular authentication policies be applied by the OpenID Provider when authenticating an End User. This extension also provides a mechanism by which an OpenID Provider may inform a Relying Party which authentication policies were used. Thus a Relying Party can request that the End User authenticate, for example, using a phishing-resistant or multi-factor authentication method.


## How to use it? ##
Example:
```
OPENID_PAPE = {"policy_list": "http://schemas.openid.net/pape/policies/2007/06/multi-factor", "max_auth_age": 3600}
```

Basicly, a dictionary with two keys:
  * policy\_list  (str)
  * max\_auth\_age  (int)

For an explanation on why and how to use this fields, look at the [specs](http://openid.net/specs/openid-provider-authentication-policy-extension-1_0-02.html)