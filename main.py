import asyncio

import uvicorn

from fastapi_async_sqlalchemy.app import app
from fastapi_async_sqlalchemy.db import create_sa_engine, run_async_migrations
from fastapi_async_sqlalchemy.settings import get_settings


async def run_migrations() -> None:
    settings = get_settings()
    engine = create_sa_engine(settings.database_url)
    await run_async_migrations(engine)
    await engine.dispose()


def main() -> None:
    asyncio.run(run_migrations())
    uvicorn.run(app)


if __name__ == "__main__":
    main()
