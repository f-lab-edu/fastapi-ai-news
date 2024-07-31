from fastapi import FastAPI

from app.api.public import public_router

app = FastAPI()


@app.get("/")
def read_root():
    return {"test msg": "Hello World"}
