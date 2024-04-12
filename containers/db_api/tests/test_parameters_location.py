import sys
import unittest

from unittest.mock import Mock


sys.path.append("..")
sys.modules["psycopg2"] = Mock()


from api.parameters.location import LocationType, get_location


class TestLibPrices(unittest.TestCase):

    def test_location_port(self):
        location = get_location("PCODE")

        self.assertEqual(location.TYPE, LocationType.PORT)
        self.assertEqual(str(location), "PCODE")

    def test_location_region(self):
        location = get_location("some_region")

        self.assertEqual(location.TYPE, LocationType.REGION)
        self.assertEqual(str(location), "some_region")

    def test_empty_location(self):
        self.assertRaises(ValueError, get_location, "")

    def test_bad_port(self):
        self.assertRaises(ValueError, get_location, "TOOLONG")

    def test_bad_characters(self):
        self.assertRaises(ValueError, get_location, "location_with_numb3r5")
        self.assertRaises(ValueError, get_location, "location_with_???")
