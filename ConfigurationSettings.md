### Global settings: ###
| **Setting** | **Default** | **Description** |
|:------------|:------------|:----------------|
| OPENID\_TRUST\_ROOT | Current host | Which root will OpenID trust. |
| OPENID\_REDIRECT\_TO | url\_of\_app + complete/ | Where will the user get redirected after it gets authenticated.|
| OPENID\_DISALLOW\_INAMES | False       | Allow/Disallow inames |
| OPENID\_REDIRECT\_NEXT | /           | Where will the user get redirected ( if there is no ?next= parameter ) after the OpenID auth is completed. |
| OPENID\_SREG | False       | If it consists of a dictionary of keys, keys named "required" and "optional" should contain required fields. "policy\_url" key should contain an url where user can read why the requested data will be used. All keys are optional. For more info check [SimpleRegistration](SimpleRegistration.md) |
| OPENID\_AX  | False       | List of dicts that must contain keys: "type\_uri", "count", "required" and "alias". For more info look at [AttributeExchange](AttributeExchange.md)  |
| OPENID\_PAPE | False       | A dictionary with an policy\_list key that contains a comma separated list of uris and max\_auth\_age key that specifies the max auth age, for more info look at [Pape](Pape.md) |

### View specific settings: ###
| **View** | **Argument** | **Default** | **Description** |
|:---------|:-------------|:------------|:----------------|
| django\_openid\_consumer.views.begin | redirect\_to | OPENID\_REDIRECT\_TO | Where will the user get redirected after it gets authenticated. |
| django\_openid\_consumer.views.begin | on\_failure  | default\_on\_failure | Which function will get called when an failure happens. |
| django\_openid\_consumer.views.begin | template\_name | openid\_signin.html | Which template will be used for begining of user auth. (basicly, consist of one form, look at [ExampleTemplates](ExampleTemplates.md)) |
| django\_openid\_consumer.views.complete | on\_success  | default\_on\_success | Which function will get called when the auth is successfuly completed. |
| django\_openid\_consumer.views.complete | on\_failure  | default\_on\_failure | Which function will get called when an failure happens. |
| django\_openid\_consumer.views.complete | failure\_template | openid\_failure.html | Which template will be used when an failure happens.([ExampleTemplates](ExampleTemplates.md)) |

#### Note: ####
[i-names](http://www.inames.net/) are part of the OpenID 2.0 specification, which is currently being developed. They are supported by the python-openid library.
You can tell if an OpenID is an i-name by checking the request.openid.is\_iname property.