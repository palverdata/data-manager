import requests

from data_manager.config import config


def count_documents(collection) -> int:
    res = requests.get(
        f"{config.solr_url}/solr/{collection}/select?q=*:*&rows=0&wt=json",
        auth=(config.solr_username, config.solr_password),
    )

    res.raise_for_status()

    return res.json()["response"]["numFound"]
