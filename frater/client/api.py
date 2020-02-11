import requests


class API:
    def __init__(self, host, port, protocol='http://'):
        self.host = host
        self.port = port
        self.protocol = protocol

    @property
    def api_url(self):
        return f'{self.protocol}{self.host}:{self.port}'

    def build_endpoint_url(self, endpoint: str):
        if not endpoint.startswith('/'):
            endpoint = '/' + endpoint

        return f'{self.api_url}{endpoint}'

    def get(self, endpoint: str, params=None):
        endpoint_url = self.build_endpoint_url(endpoint)
        response = requests.get(endpoint_url, params=params)
        return response.json()

    def post(self, endpoint: str, data: dict):
        endpoint_url = self.build_endpoint_url(endpoint)
        response = requests.post(endpoint_url, json=data)
        return response.json()

    def delete(self, endpoint: str, data: dict):
        endpoint_url = self.build_endpoint_url(endpoint)
        response = requests.delete(endpoint_url, json=data)
        return response.json()

    def patch(self, endpoint: str, data: dict):
        endpoint_url = self.build_endpoint_url(endpoint)
        response = requests.patch(endpoint_url, json=data)
        return response.json()

    def put(self, endpoint: str, data: dict):
        endpoint_url = self.build_endpoint_url(endpoint)
        response = requests.put(endpoint_url, json=data)
        return response.json()
