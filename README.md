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
```
curl http://localhost:8000/rates\?date_from\=2000-01-01\&date_to\=2020-12-31\&origin\=china_main\&destination\=north_europe_main
[{"average_prices":1164,"day":"2016-01-01"},{"average_prices":1164,"day":"2016-01-02"},{"average_prices":1193,"day":"2016-01-05"},{"average_prices":1192,"day":"2016-01-06"},{"average_prices":1195,"day":"2016-01-07"},{"average_prices":1189,"day":"2016-01-08"},{"average_prices":1189,"day":"2016-01-09"},{"average_prices":1189,"day":"2016-01-10"},{"average_prices":1157,"day":"2016-01-11"},{"average_prices":1124,"day":"2016-01-12"},{"average_prices":1122,"day":"2016-01-13"},{"average_prices":1120,"day":"2016-01-14"},{"average_prices":1105,"day":"2016-01-15"},{"average_prices":1103,"day":"2016-01-16"},{"average_prices":1103,"day":"2016-01-17"},{"average_prices":1082,"day":"2016-01-18"},{"average_prices":1073,"day":"2016-01-19"},{"average_prices":1052,"day":"2016-01-20"},{"average_prices":1050,"day":"2016-01-21"},{"average_prices":1023,"day":"2016-01-22"},{"average_prices":1021,"day":"2016-01-23"},{"average_prices":1017,"day":"2016-01-24"},{"average_prices":997,"day":"2016-01-25"},{"average_prices":968,"day":"2016-01-26"},{"average_prices":967,"day":"2016-01-27"},{"average_prices":968,"day":"2016-01-28"},{"average_prices":962,"day":"2016-01-29"},{"average_prices":962,"day":"2016-01-30"},{"average_prices":961,"day":"2016-01-31"},{"average_prices":null,"day":"2016-01-04"}]
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
