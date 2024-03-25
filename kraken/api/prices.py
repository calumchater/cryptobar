

from typing import Any, List

from .types import Price

from .errors import ApiNotEnabled

from .client import Client


class Prices:



    def __init__(self, client: Client):
        self.client = client

    def get_prices(self, ticker: str) -> List[Price]:
        breakpoint()
        open_orders_endpoint = "/0/public/Ticker"

        params = {"pair": ticker}

        return self._from_dict(self.client.get(path=open_orders_endpoint, params=params), ticker)

    def _from_dict(self, data: dict, key: str) -> List[Price]:
        breakpoint()
        if data.get("error"):
            raise ApiNotEnabled(data["error"]["code"], data["error"]["message"])
        else:
            return [Price(i) for i in data["result"][key]]  # items or sth
