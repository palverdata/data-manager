from pymongo import MongoClient

from data_manager.models.model import CLIENT_NAME
from data_manager.utils import mongourl_replace


def connect(url: str, ignore_database_name: bool = False) -> MongoClient:
    """Setup data manager connection using mongoflex.

    By default it will change the database name to `data_manager.models.CLIENT_NAME`, if
    you to disable this behaviour, set `ignore_database_name` to `True`."""
    if not ignore_database_name:
        url = mongourl_replace(url, database=CLIENT_NAME)

    from mongoflex.connection import connect as _connect

    return _connect(host=url, client_name=CLIENT_NAME)
