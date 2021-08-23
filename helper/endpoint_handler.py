import logging
import pytest
from API_Test.utilities.request import APIRequests


class api_crud:
    logger = logging.getLogger()
    logger.setLevel("INFO")

    def getResponseFormat(self, getData):
        resp = APIRequests.get(getData['base_url'], getData["fromAndlimit"])
        if list(resp.json()[0].keys()) != getData['getstation_resp_model']:
            self.logger.info("Response dones't match expected format as per API Documentation")
            pytest.fail("Response dones't match expected format as per API Documentation")

    def getStations(self, getData, using=''):
        if using == 'fromAndLimit':
            resp = APIRequests.get(getData['base_url'], getData["fromAndlimit"])
            if len(resp.json()) != getData['fromAndlimit']['limit']:
                self.logger.info("Response length not matching expected length")
                pytest.fail("Response length not matching expected length")
            self.logger.info("Test Get Stations with 'From' query string Passed")

        elif using == 'limit':
            resp = APIRequests.get(getData['base_url'], getData["limit"])
            if resp.json()['message'] != "The given data was invalid.":
                self.logger.info("Response length not matching expected length")
                pytest.fail("Response length not matching expected length")
            self.logger.info("Test Get Stations with 'Limit' query string Passed")

        elif using == 'coordinates':
            resp = APIRequests.get(getData['base_url'], getData['coordinates'])
            if resp.json() and resp.json()[0]['latitude'] < getData['coordinates']['latMax']:
                self.logger.info("Test Get Stations with Coordinates API Passed")
            else:
                self.logger.info("No Results matching Query")
                pytest.fail("No Results matching Query")
