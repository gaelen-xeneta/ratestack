""" Handler code for the /rates URI."""

# import API application modules
from api import APP, request
from api.parameters import process_request_parameters
from api.parameters.location import LocationType
from api.lib.prices import aggregate_prices

# import database interactions
from api.db.port_codes import get_region_port_codes
from api.db.prices import get_prices


@APP.route("/rates", methods=["GET"])
def get_rates():
    """Handler code for the GET method."""
    # process request parameters and log the results
    args = process_request_parameters(request.args.to_dict())
    APP.logger.debug(str(args))

    # turn origin location into a list of port codes
    if args["origin"].TYPE == LocationType.REGION:
        origin_port_codes = get_region_port_codes(args["origin"])
    else:
        origin_port_codes = [args["origin"]]
    APP.logger.debug("origin port codes: " + str(origin_port_codes))

    # turn destination location into a list of port codes
    if args["destination"].TYPE == LocationType.REGION:
        destination_port_codes = get_region_port_codes(args["destination"])
    else:
        destination_port_codes = [args["destination"]]
    APP.logger.debug("destination port codes: " + str(destination_port_codes))

    # get price data for origin/destination pairs during the specified date range
    prices = get_prices(
        origin_port_codes,
        destination_port_codes,
        args["date_from"],
        args["date_to"],
    )

    # aggregate pricing data
    aggregated = aggregate_prices(prices)
    APP.logger.debug(aggregated)

    return aggregated
