from dataclasses import dataclass
from typing import Literal, Optional

from bson import ObjectId
from mongoflex import Model
from pymongo import IndexModel

_ShardOption = Literal["cra_time"]


@dataclass
class SolrConfig(Model):
    """Configuration that controls solr related tasks like autosharding."""

    data_source_id: ObjectId

    collection: str

    shard_key: str = None
    shard_type: Optional[_ShardOption] = None
    shard_threshold: int = 10_000_000

    INDEXES = [
        IndexModel([("data_source_id", 1)], unique=True),
    ]

    @property
    def current_shard_collection(self) -> str:
        if self.shard_type == "cra_time":
            return f"{self.collection}__CRA__{self.shard_key}"

        return self.collection
