# Async SQLAlchemy Core + Alembic + FastAPI

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![mypy: checked](https://img.shields.io/badge/mypy-checked-green)](http://mypy-lang.org)
[![codecov](https://codecov.io/gh/ijohn/fastapi-async-sqlalchemy/branch/main/graph/badge.svg?token=6tvbtYUnHd)](https://codecov.io/gh/ijohn/fastapi-async-sqlalchemy)

This repository shows a very simple example on how to create an all async project using FastAPI, SQLAlchemy Core (not ORM), and Alembic.

DB migrations are done automatically upon [application start](https://github.com/ijohn/fastapi-async-sqlalchemy/blob/3baa8edf7791e7151a0c2b69bd466061988b62a3/main.py#L18). However, `alembic upgrade head` works perfectly too.
