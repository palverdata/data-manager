from os import getenv
from typing import Protocol

from dotenv import load_dotenv


class ConfigProtocol(Protocol):
    solr_url: str
    mongo_url: str
    solr_username: str
    solr_password: str


class Config:
    def __init__(self) -> None:
        load_dotenv()

    def __getattr__(self, name: str):
        return getenv(name.upper())


config = Config()
