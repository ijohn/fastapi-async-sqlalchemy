from alembic import command, config
from sqlalchemy.ext.asyncio import AsyncConnection, create_async_engine

from settings import get_settings

engine = create_async_engine(get_settings().database_url, connect_args={"check_same_thread": False}, echo=True)


def run_upgrade(connection, cfg):
    cfg.attributes["connection"] = connection
    command.upgrade(cfg, "head")


async def run_async_migrations():
    async with engine.begin() as conn:
        await conn.run_sync(run_upgrade, config.Config("alembic.ini"))


async def get_connection() -> AsyncConnection:
    async with engine.connect() as conn:
        yield conn
