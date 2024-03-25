import os
from dotenv import load_dotenv
import sched
import time

from newsAPI.search import Search
from newsAPI.adapter import RequestsAdapter


load_dotenv()

from litestar import Litestar, get


@get("/articles")
async def articles():
    # Returns a list of the articles we've processed    
    articles = []

    return articles

def fetch_news_articles():
    search_client = Search(RequestsAdapter(os.environ.get('GOOGLE_SEARCH_KEY'), os.environ.get('GOOGLE_ENGINE_ID')))
    search_client.search()
    breakpoint()



scheduler = sched.scheduler(time.time, time.sleep)

def repeat_task():
    scheduler.enter(5, 30, fetch_news_articles, ())
    scheduler.enter(5, 1, repeat_task, ())

repeat_task()
scheduler.run()


app = Litestar(route_handlers=[articles])