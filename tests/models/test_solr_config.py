from bson import ObjectId

from data_manager.models.solr_config import SolrConfig


def test_current_shard_collection():
    cfg = SolrConfig(
        data_source_id=ObjectId(),
        collection="test",
        shard_key="2021_01_01",
        shard_type="cra_time",
    )

    assert cfg.current_shard_collection == "test__CRA__2021_01_01"
