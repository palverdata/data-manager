from dataclasses import dataclass
from typing import Optional

from data_manager.models.model import Model


@dataclass
class MediaProcessingConfig(Model):
    source: str

    solr_collection: str
    mongo_collection: str

    primary_key: Optional[str] = "id"
    solr_primary_key: Optional[str] = None
