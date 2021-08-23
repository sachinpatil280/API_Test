import pytest
from API_Test.utilities.readProperties import ReadConfig

fixtureUI = None

@pytest.fixture()
def getData():
    query_string = ReadConfig.readConfig_yamlFile('test_data')
    return query_string