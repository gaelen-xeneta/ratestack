# Overview

This project provides a basic solution to the [Xeneta ratestask](https://github.com/xeneta/ratestask) problem.

## Setup

All that is needed to get started is to have Docker Desktop (or equivalent) installed. Executing the `run` script from a terminal in the root directory will use the configured environment shell to run `docker compose` commands and start the application.

Once the containers are running navigate to `http://localhost:8000/rates` in a browser, or use a tool like `curl` to query the endpoint:
```
http://localhost:8000/rates?date_from=2016-01-01&date_to=2016-01-10&origin=CNSGH&destination=north_europe_main
[
  {
    "average_prices": 1111,
    "day": "2016-01-01"
  },
  {
    "average_prices": 1112,
    "day": "2016-01-02"
  },
  {
    "average_prices": 1141,
    "day": "2016-01-05"
  },
  {
    "average_prices": 1141,
    "day": "2016-01-06"
  },
  {
    "average_prices": 1136,
    "day": "2016-01-07"
  },
  {
    "average_prices": 1124,
    "day": "2016-01-08"
  },
  {
    "average_prices": 1124,
    "day": "2016-01-09"
  },
  {
    "average_prices": 1124,
    "day": "2016-01-10"
  },
  {
    "average_prices": null,
    "day": "2016-01-04"
  }
]
```

# Design

This prototype runs two docker containers. The PostgreSQL container provided in the [Xeneta ratestask](https://github.com/xeneta/ratestask) repository, and a Flask application running in a `python:3.10-alpine` container.

Each container is defined in its own subdirectory.
```
.
├── run                # Simple executable shell script to build and start containers
├── compose.yml
└── containers/
    ├── db/            # PostgreSQL database container provided by Xeneta
    └── db_api/        # Flask application providing low level HTTP API
```
