import logging
import os
from functools import lru_cache
from pydantic import BaseSettings, AnyUrl


log = logging.getLogger("uvicorn")


class Settings(BaseSettings):
  environment: str = os.getenv("ENVIRONMENT", "dev")
  testing: bool = os.getenv("TESTING", 0)
  database_url: AnyUrl = os.getenv("DATABASE_URL")

# Let's use lru_cache to cache the settings so get_settings is only called once.
@lru_cache()
def get_settings() -> BaseSettings:
  log.info("Loading config settings from the environment...")
  return Settings()
