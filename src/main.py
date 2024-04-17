from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routes import blogs

app = FastAPI()

app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

app.include_router(blogs.router)

@app.get("/")
async def root():
  return {"data" : "fastapi-money-tracker-site"}