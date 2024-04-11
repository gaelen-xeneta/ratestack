# Database API

A simple Flask application that provides a low level HTTP based API for interacting with a PostgreSQL database.

Supports the following URIs:
```
/rates [GET]
```

## Design

This Docker container is provided as a `Dockerfile` describing the container, a `requirements.txt` file listing external Python package dependencies, an `api` directory that contains the application code, and a `sql_templates` directory that provides common SQL queries with Python format fields.

```
.
├── Dockerfile
├── requirements.txt        # Python package requirements
├── api/
│   ├── __init__.py            # API application entry point
│   ├── application.py         # Flask application definition
│   ├── db/                    # Database interaction code (create connections, make queries, etc.)
│   ├── lib/                   # Application library code
│   ├── parameters/            # Request parameter code (input checking, type transformations, etc.)
│   └── routes/                # API route definitions
│       └── rates/               # /rates URI handler
└── sql_templates/          # SQL query templates
```

## Future Considerations

Ideally this API would support JSON schemas. However, as it currently only supports a single read-only API it is not worth the effort to implement.
