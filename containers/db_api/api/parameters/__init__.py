from .date import get_date
from .location import get_location


def process_request_parameters(request_parameters: dict):
    """Process request parameters by converting them to objects using factory
    methods"""
    args = {
        "date_from": get_date(request_parameters["date_from"]),
        "date_to": get_date(request_parameters["date_to"]),
        "origin": get_location(request_parameters["origin"]),
        "destination": get_location(request_parameters["destination"]),
    }
    return args
