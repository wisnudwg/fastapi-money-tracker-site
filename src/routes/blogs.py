from fastapi import APIRouter
from src.models.blogs import Blog
from src.databases import collection_name
from src.schemas.blogs import serialize_blogs
from bson import ObjectId

router = APIRouter(
  prefix="/blogs",
  tags=["Blogs"],
)

# Get top blogs
@router.get("")
async def get_top_blogs():
  blogs = []
  ids = [1,2,3,4,5]
  for id in ids:
    blogs.append({
      "id": id,
      "title": f"Article {id}",
      "metadata": f"metadata of article {id}",
      "body": f"Body of article {id}",
    })
  return blogs

@router.get("/{id}")
async def get_blog_by_id(id: int):
  return {
    "id": id,
    "title": f"Article {id}",
    "metadata": f"metadata of article {id}",
    "body": f"Body of article {id}",
  }

# # GET request method
# @router.get("")
# async def get_blogs():
#   blogs = serialize_blogs(collection_name.find())
#   return blogs
# 
# #POST request method
# @router.post("")
# async def post_blog(blog: Blog):
#   collection_name.insert_one(dict(blog))
# 
# #PUT request method
# @router.put("/{id}")
# async def put_blog(id: str, blog: Blog):
#   collection_name.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(blog)})
# 
# #DELETE request method
# @router.delete("/{id}")
# async def delete_blog(id: str):
#   collection_name.find_one_and_delete({"_id": ObjectId(id)})