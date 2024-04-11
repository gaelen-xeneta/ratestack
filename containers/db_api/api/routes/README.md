# Overview

Hierarchical route definitions for the API application.

## Design

Handlers are organized by the URI they support.

```
.
└── routes/
    ├── __init__.py        # Module file
    └── rates/             # /rates URI handlers
        └── __init__.py      # /rates method handlers
```

## Future Considerations

Additional routes can be easily added and kept organized by using file paths that mimic the URI tree. Each HTTP method can be handled in it's own function.

If the `/rates` handler was extended to support more methods it would look like:
```
from api import APP, request
...

@APP.route("/rates", methods=[GET])
def get_rates:
    ...

APP.route("/rates", methods=[POST])
def post_rates:
    ...

...
```

### Handler Code Templating

Minor adjustments to the handler decorator code could be made to provide a basic method handler template that uses the local files path to the root `routes` directory to define the route.
Example:
```
from api import APP, request
...

@APP.route(<path>, methods=[<method>])
def <method>_<escaped_path>:
    ...
```
