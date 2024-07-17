from fastapi import FastAPI

from app.api.public import public_router

app = FastAPI()

app.include_router(public_router, prefix="/api", tags=["Public"])


@app.get("/")
def read_root():
    return {"test msg": "Hello World"}
