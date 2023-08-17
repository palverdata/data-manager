from datetime import datetime

from data_manager.entrypoint import Entrypoint
from data_manager.logger import logger
from data_manager.models.solr_config import SolrConfig
from data_manager.solr import count_documents


class ChangeCRAKeyJob:
    """Change the CRA key for a given shard.

    This job looks into every collection configured with 'cra_time' as the `shard_type`
    and verifies that the threshold is not exceeded. If it is, it will change the shard
    key to the current utc time in the format of 'YYYY-MM-DDTHH:MM:SSZ'. This will mark
    the next shard key until the threshold is exceeded again.
    """

    def _change_cra_key(self, config: SolrConfig):
        """Change the shard key for a given config."""

        total = count_documents(config.current_shard_collection)

        logger.info(
            f"Current shard key for {config.collection} is {config.shard_key} "
            f"with {total} documents"
        )

        if total >= config.shard_threshold:
            now = datetime.utcnow()

            logger.info(f"Changing shard key for {config.collection} to {now}")

            config.update(
                shard_key=now.strftime("%Y-%m-%dT%H:%M:%SZ"),
            )

    def perform(self):
        with Entrypoint():
            for config in SolrConfig.find({"shard_type": "cra_time"}):
                self._change_cra_key(config)
