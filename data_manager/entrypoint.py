from mongoflex import connect

from data_manager.config import ConfigProtocol, config


class Entrypoint:
    def __init__(self, cfg: ConfigProtocol = config) -> None:
        self.config = cfg

    def __enter__(self):
        connect(self.config.mongo_url)

        return self
