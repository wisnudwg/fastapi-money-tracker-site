from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
  return {"message": "connected"}

@app.get("/blogs")
async def get_top_blogs():
  ids = [1,2,3,4,5]
  blogs = []
  for id in ids:
    blogs.append({
      "id": id,
      "title": f"Article {id}",
      "meta": f"medatada of article {id}",
      "body": f"Body of article {id}",
    })
  return blogs

@app.get("/blog/{id}")
async def get_blog_by_id(id: int):
  return {
    "id": id,
    "title": f"Article {id}",
    "meta": f"metadata of article {id}",
    "body": f"Body of article {id}",
  }