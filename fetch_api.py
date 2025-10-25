import requests
from pyarrow.lib import JsonType


class fetch_api:
    def __init__(self, url: str):
        self.url = url
    def get_desired_data(self, ask: str) -> JsonType:
        data = requests.get(self.url + ask)
        if data.status_code == 200:
            return data.json()
        else:
            raise ConnectionError("Something went wrong")