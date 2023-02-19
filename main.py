from fastapi import Depends, FastAPI
from app.config.config import get_settings, Settings

app = FastAPI()


# get_settings gets called for each request
@app.get("/ping")
async def pong(settings: Settings = Depends(get_settings)):
    return {
            "ping": "pong!",
            "environment": settings.environment,
            "testing": settings.testing
            }
