import sys
import unittest

from unittest.mock import MagicMock, Mock, patch


sys.path.append("..")
sys.modules["psycopg2"] = Mock()


import api

from api.db.prices import get_prices


class TestDBPortCodes(unittest.TestCase):

    def setUp(self):
        # Set up some placeholder query strings
        api.db.prices.QUERIES = {
            "get_prices": "{origins} {destinations} {date_from} {date_to}",
        }

        # Set up connection and cursor mocks
        self.cursor_mock = Mock(name="cursor")
        self.connection_mock = Mock(name="connection")
        self.connection_mock.cursor = Mock(return_value=self.cursor_mock)

        # Replace the db_conn object on APP with the mock
        api.db.port_codes.APP.db_conn = self.connection_mock

    def test_normal_behavior(self):
        self.cursor_mock.fetchall = MagicMock(return_value=["some_region"])
        get_prices(["origins"], ["destinations"], ["date_from"], ["date_to"])
