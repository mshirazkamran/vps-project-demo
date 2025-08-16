from fastapi import FastAPI
import logging
from contextlib import asynccontextmanager
import uvicorn

from .todos import service
from src.todos import router

# Configure logging
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

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

if __name__ == "__main__":
    uvicorn.run(app=app, host="127.0.0.1", port=8000)
