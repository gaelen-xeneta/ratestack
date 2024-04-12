import sys
import unittest

from unittest.mock import Mock


sys.path.append("..")
sys.modules["psycopg2"] = Mock()


from api.lib.prices import aggregate_prices


DATA = [
    ("ABCDE", "VWXYZ", "2020-07-17", 800),
    ("ABCDE", "VWXYZ", "2020-07-17", 800),
    ("ABCDE", "VWXYZ", "2020-07-17", 800),
    ("ABCDE", "QRSTU", "2020-07-18", 500),
    ("ABCDE", "QRSTU", "2020-07-18", 500),
    ("ABCDE", "LMNOP", "2020-07-20", 500),
]


class TestLibPrices(unittest.TestCase):

    def test_average_price(self):
        aggregated = aggregate_prices(DATA)

        self.assertEqual(aggregated[0]["day"], "2020-07-17")
        self.assertEqual(aggregated[0]["average_price"], 800)

    def test_null_price(self):
        aggregated = aggregate_prices(DATA)

        self.assertEqual(aggregated[1]["day"], "2020-07-18")
        self.assertEqual(aggregated[1]["average_price"], None)

        self.assertEqual(aggregated[2]["day"], "2020-07-20")
        self.assertEqual(aggregated[2]["average_price"], None)
