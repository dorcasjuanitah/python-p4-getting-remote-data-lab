import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(url)
        return response.text

    def load_json(self):
        response_body = self.get_response_body()
        return response.json()