from fastapi import APIRouter, HTTPException
from src.models.blogs import Blog
from src.databases import collection_name
from src.schemas.blogs import serialize_blog, serialize_blogs
from bson import ObjectId

router = APIRouter(
  prefix="/blogs",
  tags=["Blogs"],
)

# Get blogs
@router.get("")
async def get_blogs():
  blogs = serialize_blogs(collection_name.find())
  return blogs

@router.get("/{id}")
async def get_blog_by_id(id: str):
  try:
    blog = serialize_blog(collection_name.find_one({"_id": ObjectId(id)}))
    return blog
  except:
    raise HTTPException(status_code=404, detail="not found")

# Add new blog
@router.post("")
async def post_blog(blog: Blog):
  try:
    collection_name.insert_one(dict(blog))
    return {"message": "insert success"}
  except:
    raise HTTPException(status_code=400, detail="failed to insert")

# Edit an existing blog
@router.put("/{id}")
async def put_blog(id: str, blog: Blog):
  try:
    collection_name.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(blog)})
    return {"message": "update success"}
  except:
    raise HTTPException(status_code=400, detail="failed to update")

# Delete an existing blog
@router.delete("/{id}")
async def delete_blog(id: str):
  try:
    collection_name.find_one_and_delete({"_id": ObjectId(id)})
    return {"message": "delete success"}
  except:
    raise HTTPException(status_code=400, detail="failed to delete")