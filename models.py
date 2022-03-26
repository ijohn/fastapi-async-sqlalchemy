from sqlalchemy import Column, DateTime, Integer, MetaData, String, Table

metadata = MetaData()

products = Table(
    "products",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String, nullable=False),
    Column("created_at", DateTime, nullable=False),
    Column("modified_at", DateTime, nullable=False),
)
