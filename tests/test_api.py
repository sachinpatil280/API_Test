import pytest
import logging

from API_Test.helper.endpoint_handler import api_crud

logger = logging.getLogger()
logger.setLevel("INFO")

api = api_crud()


@pytest.mark.regression
def test_getStationsResponseFormat(getData):
    """
    Here we are trying to test response and compare with data model shown on API Documentation
    """
    api.getResponseFormat(getData)


@pytest.mark.regression
def test_getStationsUsingFromAndLimit(getData):
    """
    Here we are trying to test GET /stations api with query string: "from" and "limit
    """
    api.getStations(getData, 'fromAndLimit')


@pytest.mark.regression
def test_getStationsUsingLimit(getData):
    """
    Here we are trying to test GET /stations api with query string: "limit"
    """
    api.getStations(getData, 'limit')


@pytest.mark.regression
def test_getStationUsingCoordinates(getData):
    """
    Here we are trying to test GET /stations api with query string: "latMin", "latMax", "longMin", "longMax"
    """
    api.getStations(getData, 'coordinates')
