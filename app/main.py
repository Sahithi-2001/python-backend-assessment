from fastapi import FastAPI
from .routes import router

app = FastAPI(title="GitHub Task Tracker")

app.include_router(router)
