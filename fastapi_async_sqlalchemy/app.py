from datetime import datetime
from typing import Any

from fastapi import Depends, FastAPI
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncConnection

from fastapi_async_sqlalchemy.db import get_connection, run_async_migrations
from fastapi_async_sqlalchemy.models import products
from fastapi_async_sqlalchemy.schemas import Product, ProductCreate, ProductList, TimestampsMixin

app = FastAPI()


@app.on_event("startup")
async def on_startup():
    await run_async_migrations()


def get_timestamps_dict(dt: datetime) -> dict[str, Any]:  # pylint: disable=invalid-name
    return TimestampsMixin(created_at=dt, modified_at=dt).dict()


@app.get("/products", response_model=ProductList, response_model_by_alias=True)
async def list_products(conn: AsyncConnection = Depends(get_connection)) -> ProductList:
    result = await conn.execute(select(products))
    product_rows = result.fetchall()
    return ProductList(products=[Product.parse_obj(row) for row in product_rows])


@app.post("/products", response_model=Product, response_model_by_alias=True)
async def create_product(product_data: ProductCreate, conn: AsyncConnection = Depends(get_connection)) -> Product:
    query = products.insert()
    insert_result = await conn.execute(query, product_data.dict() | get_timestamps_dict(datetime.utcnow()))
    await conn.commit()
    select_result = await conn.execute(products.select().where(products.c.id == insert_result.inserted_primary_key[0]))
    new_product_row = select_result.fetchone()
    return Product.parse_obj(new_product_row)
