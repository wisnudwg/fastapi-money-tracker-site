def serialize_blog(blog) -> dict:
  return {
    "id": str(blog["_id"]),
    "title": blog["title"],
    "metadata": blog["metadata"],
    "body": blog["body"],
  }

def serialize_blogs(blogs) -> list:
  return [serialize_blog(blog) for blog in blogs]