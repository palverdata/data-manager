from dataclasses import dataclass

from pymongo import IndexModel

from data_manager.models import Model


@dataclass
class DataSource(Model):
    name: str
    description: str

    INDEXES = [
        IndexModel([("name", 1)], unique=True),
    ]
