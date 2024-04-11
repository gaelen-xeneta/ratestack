from collections import defaultdict


def aggregate_prices(prices: list):
    collected = defaultdict(list)

    for _, _, date, price in prices:
        collected[date].append(price)

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
