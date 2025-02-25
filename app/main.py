import os

import redis
from fastapi import FastAPI
from fastapi_socketio import SocketManager
from sqlalchemy import create_engine

app = FastAPI()
socket_manager = SocketManager(app=app)

# Use environment variables set in docker-compose.yml
DATABASE_URL = os.getenv("DATABASE_URL")
REDIS_URL = os.getenv("REDIS_URL")

# Ensure environment variables are set
if not DATABASE_URL:
    raise ValueError("ERROR: DATABASE_URL environment variable is not set.")
if not REDIS_URL:
    raise ValueError("ERROR: REDIS_URL environment variable is not set.")

# Get SQLAlchemy engine
engine = create_engine(DATABASE_URL)


# Get Redis connection
def get_redis():
    try:
        return redis.Redis.from_url(REDIS_URL, decode_responses=True)
    except redis.RedisError as e:
        print(f"Redis connection failed: {e}")
        return None


# Create a Redis client
redis_client = get_redis()


@app.get("/")
def read_root():
    return {"message": "Gender Reveal Puzzle Backend is Running!"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
