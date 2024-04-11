from flask import abort

from .date import get_date
from .location import get_location


def process_request_parameters(request_parameters: dict):
    """Process request parameters by converting them to objects using factory methods."""
    try:
        args = {
            "date_from": get_date(request_parameters["date_from"]),
            "date_to": get_date(request_parameters["date_to"]),
            "origin": get_location(request_parameters["origin"]),
            "destination": get_location(request_parameters["destination"]),
        }

    except KeyError as error:
        abort(400, f"Missing required parameter: {error}")

    except ValueError as error:
        abort(400, f"Unable to parse parameter value: {error}")

    return args
