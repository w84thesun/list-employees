import uvicorn

from fastapi import FastAPI
from app.router.router import api

app = FastAPI()

app.include_router(api, prefix="/employee")

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
