import requests


class APIRequests:

    @staticmethod
    def get(url, data=None):
        """
        :param url: Endpoint of the API
        :param data:  Containing values to pass with url through query string. It can be dictonary, list of tuples or bytes.
        :return: response
        """
        response = requests.get(url, params=data)
        return response

    @staticmethod
    def post(url, data=None):
        """
        :param url: Endpoint of the API
        :param data:  Containing values to pass with url through query string. It can be dictonary, list of tuples or bytes.
        :return: response
        """
        response = requests.post(url, data=data)
        return response

    @staticmethod
    def put(url, data=None):
        """
        :param url: Endpoint of the API
        :param data:  Containing values to pass with url through query string. It can be dictonary, list of tuples or bytes.
        :return: response
        """

        response = requests.put(url, data=data)
        return response

    @staticmethod
    def patch(url, data=None):
        """
        :param url: Endpoint of the API
        :param data:  Containing values to pass with url through query string. It can be dictonary, list of tuples or bytes.
        :return: response
        """
        response = requests.patch(url, data=data)
        return response

    @staticmethod
    def delete(url):
        """
        :param url: Endpoint of the API
        :return: response
        """
        response = requests.delete(url)
        return response

    @staticmethod
    def options(url):
        """
        :param url: Endpoint of the API
        :return: response
        """

        response = requests.options(url)
        return response
