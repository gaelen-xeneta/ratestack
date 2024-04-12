import sys
import unittest

from unittest.mock import MagicMock, Mock, patch


sys.path.append("..")
sys.modules["psycopg2"] = Mock()


import api

from api.db.port_codes import get_region_port_codes


class TestDBPortCodes(unittest.TestCase):

    def setUp(self):
        # Set up some placeholder query strings
        api.db.port_codes.QUERIES = {
            "get_region_children": "{slug}",
            "get_region_ports": "{slugs}",
        }

        # Set up connection and cursor mocks
        self.cursor_mock = Mock(name="cursor")
        self.connection_mock = Mock(name="connection")
        self.connection_mock.cursor = Mock(return_value=self.cursor_mock)

        # Replace the db_conn object on APP with the mock
        api.db.port_codes.APP.db_conn = self.connection_mock

    def test_normal_behavior(self):
        self.cursor_mock.fetchall = MagicMock(return_value=["some_region"])
        get_region_port_codes("some_region")

    def test_bad_region_slug(self):
        self.cursor_mock.fetchall = MagicMock(return_value=[])

        with self.assertRaises(Exception) as cm:
            get_region_port_codes("not_a_real_region")

        self.assertEqual(cm.exception.code, 400)
        self.assertEqual(cm.exception.name, "Bad Request")
