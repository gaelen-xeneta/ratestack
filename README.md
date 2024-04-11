# Overview

This project provides a basic solution to the [Xeneta ratestask](https://github.com/xeneta/ratestask) problem.

## Setup

All that is needed to get started is to have Docker Desktop (or equivalent) installed. Executing the `run` script from a terminal in the root directory will use the configured environment shell to run `docker compose` commands and start the application.

# Design

This prototype runs two docker containers. The PostgreSQL container provided in the [Xeneta ratestask](https://github.com/xeneta/ratestask) repository, and a Flask application running in a `python:3.10-alpine` container.

Each container is defined in its own subdirectory.
```
.
├── run
├── compose.yml
└── containers/
    ├── db/
    └── db_api/
```
