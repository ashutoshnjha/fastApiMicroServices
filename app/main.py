from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Greetings": "AnjLab"}


@app.get("/hit/{hit_id}")
async def hit_count(hit_id: int, query: Union[str, None] = None):
    return {"hit_id": hit_id, "query": query}
