from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
  return {"message": "connected"}

@app.get("/blog/{id}")
async def get_blog_by_id(id: int):
  return {
    "id": id,
    "title": f"Article {id}",
    "meta": f"metadata of article {id}",
    "body": f"Body of article {id}",
  }