import asyncio
import os

import pytest
from fastapi import FastAPI
from pytest_mock import MockerFixture

from fastapi_async_sqlalchemy.app import app
from fastapi_async_sqlalchemy.db import create_sa_engine, run_async_migrations
from fastapi_async_sqlalchemy.settings import Settings, get_settings


def get_test_file_path() -> str:
    return "./test.db"


def pytest_configure() -> None:
    test_file_path = get_test_file_path()
    if os.path.exists(test_file_path):
        os.remove(test_file_path)


@pytest.fixture(scope="session")
def event_loop() -> asyncio.AbstractEventLoop:
    return asyncio.get_event_loop_policy().get_event_loop()


@pytest.fixture(autouse=True)
def mock_env_vars(mocker: MockerFixture) -> None:
    mocker.patch.dict(os.environ, {"database_url": f"sqlite+aiosqlite:///{get_test_file_path()}"})


@pytest.fixture(name="settings")
def fixture_settings() -> Settings:
    return get_settings()


async def run_migrations(settings: Settings) -> None:
    engine = create_sa_engine(settings.database_url)
    await run_async_migrations(engine)
    await engine.dispose()


@pytest.fixture(name="app")
async def fixture_app(settings: Settings) -> FastAPI:
    await run_migrations(settings)
    return app


@pytest.fixture(name="base_url")
def fixture_base_url() -> str:
    return "http://localhost"
