from alembic import command, config
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine


def run_upgrade(connection, cfg) -> None:
    cfg.attributes["connection"] = connection
    command.upgrade(cfg, "head")


async def run_async_migrations(engine: AsyncEngine) -> None:
    async with engine.begin() as conn:
        await conn.run_sync(run_upgrade, config.Config("alembic.ini"))


def create_sa_engine(url: str) -> AsyncEngine:
    return create_async_engine(url, connect_args={"check_same_thread": False}, echo=True)
