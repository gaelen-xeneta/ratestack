import datetime


def get_date(value: str):
    """Use the datetime library to enforce iso formatted date strings
    and convert to date objects"""
    return datetime.date.fromisoformat(value)
