from functools import cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    database_url: str


@cache
def get_settings() -> Settings:
    return Settings()
