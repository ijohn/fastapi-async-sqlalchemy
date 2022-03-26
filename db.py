from sqlalchemy.ext.asyncio import AsyncConnection, create_async_engine

DATABASE_URL = "sqlite+aiosqlite:///./main.db"
engine = create_async_engine(DATABASE_URL, connect_args={"check_same_thread": False}, echo=True)


async def get_connection() -> AsyncConnection:
    async with engine.connect() as conn:
        yield conn
