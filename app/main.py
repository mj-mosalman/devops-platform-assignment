from fastapi import FastAPI, HTTPException
import redis
import os

app = FastAPI()

redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST", "redis"),
    port=int(os.getenv("REDIS_PORT", 6379)),
    db=0,
    decode_responses=True,
)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/")
def read_root():
    value = redis_client.get("example_key")
    if value is None:
        raise HTTPException(status_code=404, detail="Key not found")
    return {"message": value}

@app.post("/write/{key}")
def write_to_redis(key: str, value: str):
    redis_client.set(key, value)
    return {"message": f"Key '{key}' set to '{value}'"}

@app.get("/read/{key}")
def read_from_redis(key: str):
    value = redis_client.get(key)
    if value is None:
        raise HTTPException(status_code=404, detail="Key not found")
    return {"message": value.decode()}
