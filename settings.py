from pydantic import BaseSettings


class Settings(BaseSettings):
    database_url: str


def get_settings() -> Settings:
    return Settings()
