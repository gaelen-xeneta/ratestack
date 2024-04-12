import sys
import unittest

from unittest.mock import Mock


sys.path.append("..")
sys.modules["psycopg2"] = Mock()


from api.parameters.date import get_date


class TestLibPrices(unittest.TestCase):

    def test_iso_date(self):
        get_date("2020-12-31")

    def test_bad_year(self):
        self.assertRaises(ValueError, get_date, "20-12-31")

    def test_bad_month(self):
        self.assertRaises(ValueError, get_date, "2020-13-31")

    def test_bad_day(self):
        self.assertRaises(ValueError, get_date, "2020-12-32")
