from data_manager.utils import mongourl_replace


def test_mongourl_replace():
    url = (
        "mongodb://****:****@api.sample.com.br:27017/data_manager?"
        "authSource=admin&readPreference=primary&directConnection=true&ssl=false"
    )

    assert mongourl_replace(url, database="data_manager_test") == (
        "mongodb://****:****@api.sample.com.br:27017/data_manager_test?"
        "authSource=admin&readPreference=primary&directConnection=true&ssl=false"
    )
