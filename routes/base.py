from fastapi import APIRouter
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

APP_NAME = os.getenv("APP_NAME", "Unknown")
APP_VERSION = os.getenv("APP_VERSION", "Unknown")

base_router = APIRouter(
    prefix="/base",
    tags=["base"]
)

@base_router.get("/")
async def base_route():
    return {
        "message": "This is the base route",
        "app_name": APP_NAME,
        "app_version": APP_VERSION
    }