from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
from backend.config import config
from functools import lru_cache
import random

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
def top_10(sub: str, over_18: Optional[bool] = False):
    reddit = get_settings()
    post_list = []
    post_limit = 10
    # Grab posts, have filter for nfsw
    for submission in reddit.subreddit(sub).hot(limit=post_limit):
        row = []
        if over_18:
            row.append([submission.title, submission.selftext])
        else:
            if submission.over_18:
                continue
            else:
                row.append([submission.title, submission.selftext])
        post_list.append(row)
    random_post = random.choice(post_list)
    return {"title": random_post[0][0], "punchline": random_post[0][1]}


# @app.get("/info")
# async def info(reddit: config.reddit = Depends(get_settings)):
#     return {
#         "client_id": reddit.client_id,
#         "client_secret": reddit.client_secret,
#         "user_agent": reddit.user_agent,
#     }
