from fastapi import FastAPI
from routes.base import base_router

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

app.include_router(base_router)