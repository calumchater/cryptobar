from typing import Any, List

from .types import Order

from .errors import ApiNotEnabled

from .client import Client


class Orders:

    def __init__(self, client: Client):
        self.client = client

    def get_open_orders(self):
        open_orders_endpoint = "/0/private/OpenOrders"

        data = {}

        return self._from_dict(self.client.request.post(open_orders_endpoint, data), 'open')

    def get_closed_orders(self) -> List[Order]:


        open_orders_endpoint = "/0/private/OpenOrders"

        data = {}


        return self._from_dict(self.client.post(open_orders_endpoint, data), 'closed')

    def _from_dict(self, data: dict, key: str) -> List[Order]:
        breakpoint()
        if data.get("error"):
            raise ApiNotEnabled(data["error"]["code"], data["error"]["message"])
        else:
            return [Order(i) for i in data["result"][key]]  # items or sth
