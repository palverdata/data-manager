from dataclasses import dataclass

from mongoflex import Model
from pymongo import IndexModel


@dataclass
class DataSource(Model):
    name: str
    description: str

    INDEXES = [
        IndexModel([("name", 1)], unique=True),
    ]
