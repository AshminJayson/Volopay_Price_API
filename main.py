from fastapi import FastAPI
from routers import api

app = FastAPI()
app.include_router(api.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
