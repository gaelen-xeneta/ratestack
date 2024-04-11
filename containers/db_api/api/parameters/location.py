import string
from enum import Enum


class LocationType(Enum):

    REGION = 0
    PORT = 1


class Location:

    def __init__(self, value: str):
        self.value = value

    def __repr__(self):
        return f"{self.value} [{self.TYPE.name}]"

    def __str__(self):
        return self.value


class Region(Location):

    TYPE = LocationType.REGION
    CHARS = string.ascii_lowercase + "_"


class Port(Location):

    TYPE = LocationType.PORT
    CHARS = string.ascii_uppercase


def get_location(value: str):
    if len(value) == 5 and all([c in Port.CHARS for c in value]):
        return Port(value)

    if all([c in Region.CHARS for c in value]):
        return Region(value)

    raise ValueError(f"'{value}' is not a recogized location")
