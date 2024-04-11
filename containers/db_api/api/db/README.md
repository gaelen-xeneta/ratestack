# Overview

Database interaction code for the API application.

## Design

Small code files focused on specific tasks related to database interactions. The top level of the module provides the `QUERIES` dictionary with loaded SQL templates.

```
__init__.py
connection.py      # Helper code for establishing database connections
port_codes.py      # Database query code for turning a region slug into a list of port codes
prices.py          # Database query code for looking up pricing data between ports
queries.py         # SQL template loader code
```

## Future Considerations

### Connection Closing
The application code currently does not gracefully close database connections. This is not a problem in a small two container application as all containers are stopped together, but a better implementation here would be to use a context manager object that explicitly closes connections.

### Connection Security
The username and password for accessing the database are currently hard coded into the source code. A better implementation would be to use a gpg encrypted credentials file that is loaded when the connection is being established. These credentials COULD be loaded at application startup, but loading credentials during connection object instantiation would allow for real-time credential rotation in both the database and API containers.

### Connection Stability
A retry pattern has been implemented for initially establishing a database connection, but the application currently cannot handle disconnects. This isn't a problem in a small two container application running on a single machine, but this could easily break down in larger and/or more complex environment.
