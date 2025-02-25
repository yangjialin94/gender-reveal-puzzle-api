import os

import redis
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi_socketio import SocketManager
from sqlalchemy import create_engine

# Load environment variables
load_dotenv()

app = FastAPI()
socket_manager = SocketManager(app=app)

# Use environment variables
DATABASE_URL = os.getenv("DATABASE_URL")
REDIS_URL = os.getenv("REDIS_URL")

# Ensure environment variables are set
if not DATABASE_URL:
    raise ValueError("ERROR: DATABASE_URL environment variable is not set.")
if not REDIS_URL:
    raise ValueError("ERROR: REDIS_URL environment variable is not set.")

# Get postgres engine and redis client
engine = create_engine(DATABASE_URL)
redis_client = redis.Redis.from_url(REDIS_URL)


@app.get("/")
def read_root():
    return {"message": "Gender Reveal Puzzle Backend is Running!"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
