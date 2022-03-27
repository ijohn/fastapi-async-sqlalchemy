# Async SQLAlchemy Core + Alembic + FastAPI

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![mypy: checked](https://img.shields.io/badge/mypy-checked-green)](http://mypy-lang.org)
[![codecov](https://codecov.io/gh/ijohn/fastapi-async-sqlalchemy/branch/main/graph/badge.svg?token=6tvbtYUnHd)](https://codecov.io/gh/ijohn/fastapi-async-sqlalchemy)

This repository shows a very simple example on how to create an all async project using FastAPI, SQLAlchemy Core (not ORM), and Alembic.

DB migrations are done automatically upon [application start](https://github.com/ijohn/fastapi-async-sqlalchemy/blob/main/main.py#L18). However, `alembic upgrade head` works perfectly too.

## Play With It

```
git clone git@github.com:ijohn/fastapi-async-sqlalchemy.git
cd fastapi-async-sqlalchemy
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
DATABASE_URL='sqlite+aiosqlite:///./main.db' python main.py
```

Open up your browser and visit `http://localhost:8000/docs`.
