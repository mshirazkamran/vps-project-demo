from fastapi import FastAPI
import logging
from contextlib import asynccontextmanager
import uvicorn

from src.logging.config import setup_logging

from .todos import service
from src.todos import router

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


setup_logging()
logger = logging.getLogger(__name__)


# This runs for the first time only
# code before yeild runs when the app starts
# code after yield runs before the app is going to close
@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("initializing database...")
    service.initialize_database()
    yield
    logger.info("Closing FastApi app")


app = FastAPI(title="Todo CRUD API", version="1.0.0", lifespan=lifespan)
app.include_router(router.todos)


origins = [
    "http://localhost:5173", 
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)


if __name__ == "__main__":
    uvicorn.run(app=app, host="127.0.0.1", port=8000)
