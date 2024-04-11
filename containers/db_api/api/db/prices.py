from api import APP
from api.db import QUERIES


def get_prices(origins: list, destinations: list, date_from: str, date_to: str):
    """Given a list of origin port codes, destination port codes, and a range of dates,
    return a list of pricing data."""
    cur = APP.db_conn.cursor()

    # get a list of all prices for all combinations of origin port code and destination
    # port code between the specified dates
    query = QUERIES["get_prices"].format(
        origins=", ".join([f"'{origin}'" for origin in origins]),
        destinations=", ".join([f"'{destination}'" for destination in destinations]),
        date_from=date_from,
        date_to=date_to,
    )
    APP.logger.debug("\n" + query)

    cur.execute(query)
    prices = cur.fetchall()

    cur.close()

    return prices
