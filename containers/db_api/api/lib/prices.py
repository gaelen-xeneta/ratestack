"""Process price data."""

from collections import defaultdict


def aggregate_prices(prices: list):
    """Given a list of price data entries from the database, average the data by date.
    If less than 3 datapoints exist for a specific date return None instead of an average.
    """
    collected = defaultdict(list)

    # aggregate by date - ignore origin and destination
    for _, _, date, price in prices:
        collected[date].append(price)

    # average price data for each date
    aggregated = list()
    for date, prices in collected.items():
        if len(prices) < 3:
            aggregated.append(
                {
                    "day": str(date),
                    "average_prices": None,
                }
            )
        else:
            aggregated.append(
                {
                    "day": str(date),
                    "average_prices": int(sum(prices) / len(prices)),
                }
            )

    return aggregated
