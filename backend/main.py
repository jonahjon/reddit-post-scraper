from typing import Optional
from fastapi import FastAPI, Depends
from pydantic import BaseModel
from backend.config import config
from functools import lru_cache
import numpy as np
import praw

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}


@lru_cache()
def get_settings():
    return config.reddit

@app.get("/top/{sub}")
def top_10(sub: str):
    reddit = get_settings()
    post_list = []
    post_limit = 10
    for submission in reddit.subreddit(sub).hot(limit=post_limit):
        print(submission.selftext)
        post_list.append(submission.title)
    random_post = np.random.choice(post_list, size=1, replace=False)
    print(random_post)
    return {"title": random_post[0], "punchline": "haha"}


# @app.get("/info")
# async def info(reddit: config.reddit = Depends(get_settings)):
#     return {
#         "client_id": reddit.client_id,
#         "client_secret": reddit.client_secret,
#         "user_agent": reddit.user_agent,
#     }
