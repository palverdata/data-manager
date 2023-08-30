from urllib.parse import urlsplit, urlunsplit


def mongourl_replace(mongourl: str, *, database: str):
    """Replace the database in a MongoDB URL.

    Example:
        >>> mongourl_replace("mongodb://localhost:27017/palver_whatsapp", "palver_whatsapp_test")
        'mongodb://localhost:27017/palver_whatsapp_test'
    """  # noqa: E501
    scheme, netloc, _, query, fragment = urlsplit(mongourl)

    return urlunsplit((scheme, netloc, database, query, fragment))
