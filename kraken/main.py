import sched
import time
from dotenv import load_dotenv

from db import DBManager

from api.prices import Prices
from api.client import Client
from api.orders import Orders

load_dotenv()


from litestar import Litestar, get


# @get("/prices")
async def prices():
    # Returns a list of the articles we've processed    
    prices = DBManager().get('prices')

    return prices

async def orders():
    # Returns a list of the articles we've processed    
    prices = DBManager().get('orders')

    return prices



def get_latest_prices():
    return Prices(Client()).get_prices("XBTUSD")

def get_closed_orders():
    return Orders(Client()).get_closed_orders()

breakpoint()


app = Litestar(route_handlers=[])