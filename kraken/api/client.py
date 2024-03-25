# google-custom-search - adapter

import os
import time
import urllib.parse
import hashlib
import hmac
import base64
import os

from requests import Session


class Client:

    def __init__(self, *args, **kwargs):
        self.__session = Session()
        self.API_URL = "https://api.kraken.com"
        self.API_KEY = os.environ.get("KRAKEN_API_KEY")
        self.API_SECRET = os.environ.get("KRAKEN_PRIVATE_KEY")

    def _payload_maker(self, data) -> dict:
        payload = {"nonce": self.generate_nonce()}
        return {**payload, **data}

    def build_headers(self, urlpath, data):
        signature = self.get_kraken_signature(urlpath, data)    
        return {"API-Key": self.API_KEY, "API-Sign": signature}

    def get_kraken_signature(self, urlpath, data):

        postdata = urllib.parse.urlencode(data)
        encoded = (str(data["nonce"]) + postdata).encode()
        message = urlpath.encode() + hashlib.sha256(encoded).digest()
        mac = hmac.new(base64.b64decode(self.API_SECRET), message, hashlib.sha512)  
        sigdigest = base64.b64encode(mac.digest())
        return sigdigest.decode()

    def generate_nonce(self):
        return str(int(time.time() * 1000))

    def get(self, path: str, params: dict) -> dict:
        return self.__session.request(
            'GET',
            self.API_URL + path,
            params=params
        ).json()

    def post(self, path: str, data) -> dict:
        payload=self._payload_maker(data)
        return self.__session.request(
            'POST',
            self.API_URL + path,
            data=payload,
            headers=self.build_headers(path, payload),
        ).json()
