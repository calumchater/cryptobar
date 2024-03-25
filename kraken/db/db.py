import os
from kraken.api.types import Order
from kraken.api.types import Price

import psycopg as pg
import time

from questdb.ingress import Sender, IngressError, TimestampNanos
import sys
import datetime


class DBManager:

    def __init__(self, *args, **kwargs):
        self.url = os.environ.get('QUESTDB_URL')
        self.conf = f'https::addr={os.environ.get('QUESTDB_HOST')}:{os.environ.get('QUESTDB_HOST')};token=the_secure_token;'

    def insert(self, table: str, symbols: dict, columns: dict):
        try:
            with Sender.from_conf(self.conf) as sender:
                sender.row(table, 
                           symbols=symbols, 
                           columns=columns,
                           at=TimestampNanos.now())
                sender.flush()
        except IngressError as e:
            sys.stderr.write(f'Got error: {e}\n')

    def get(self, table: str):
        # Connect to an existing QuestDB instance
        conn_str = 'user=admin password=password host=127.0.0.1 port=8812 dbname=qdb'
        with pg.connect(conn_str, autocommit=True) as connection:

            # Open a cursor to perform database operations

            with connection.cursor() as cur:

                #Query the database and obtain data as Python objects.

                cur.execute(f'SELECT * FROM {table}')
                records = cur.fetchall()
                for row in records:
                    print(row)

    def insert_prices(self, prices: dict[Price]):
        table = 'prices'

        for price in prices:
            symbols = {'pair': price.pair} 
            columns = { 'ask': price.ask,
                        'bid': price.bid,
                        'low': price.low,
                        'high': price.high,
                        'last_trade_closed': price.last_trade_closed,
                        'number_of_trades': price.volume,
                        'time': datetime.now().timestamp()}
            
            self.insert(table, symbols, columns)
            
    def insert_orders(self, orders: dict[Order]):
        table = 'orders'

        for order in orders:
            symbols={
                'pair': order.pair,
                'type': order.type}
            columns={
                'traded_price': order.price,
                'limit_price': order.limit_price,
                'qty': order.quantity,
                'trade_time': order.trade_time}
            
            self.insert(table, symbols, columns)
