from fastapi import FastAPI
import logging
from contextlib import asynccontextmanager
import uvicorn

from . import service

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("initializing database...")
    service.initialize_database()
    yield
    logger.info("Closing FastApi app")


app = FastAPI(
    title="Todo CRUD API",
    version="1.0.0",
    lifespan=lifespan
);





