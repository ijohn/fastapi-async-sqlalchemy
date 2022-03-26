from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncConnection, AsyncEngine

from fastapi_async_sqlalchemy.db import create_sa_engine
from fastapi_async_sqlalchemy.settings import Settings, get_settings


def get_engine(settings: Settings = Depends(get_settings)) -> AsyncEngine:
    return create_sa_engine(settings.database_url)


async def get_connection(engine: AsyncEngine = Depends(get_engine)) -> AsyncConnection:
    async with engine.connect() as conn:
        yield conn
