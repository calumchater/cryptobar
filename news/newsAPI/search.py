
import os
from typing import List
import requests
import json
from .types import Item
from .adapter import BaseAdapter



class Search:

    CRYPTO_KEYWORDS = ['BITCOIN', 'ETHEREUM']

    """This is the class used when using Google Custom Search.

    Args:
        adapter (BaseAdapter): Insert adapter
    """
    APIURL: str = "https://www.googleapis.com/customsearch/v1"

    def __init__(self, adapter: BaseAdapter):
        self.adapter = adapter

    def search(self) -> List[Item]:

        return self.adapter.search(self.CRYPTO_KEYWORDS)