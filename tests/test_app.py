from fastapi import FastAPI, status
from httpx import AsyncClient


async def test_app(app: FastAPI, base_url: str) -> None:
    async with AsyncClient(app=app, base_url=base_url) as client:
        response = await client.post("/products", json={"title": "Foo"})
    assert response.status_code == status.HTTP_200_OK
    json_response = response.json()
    assert "createdAt" in json_response
    assert "modifiedAt" in json_response
    assert json_response["title"] == "Foo"

    async with AsyncClient(app=app, base_url=base_url) as client:
        response = await client.post("/products", json={"title": "Bar"})
    assert response.status_code == status.HTTP_200_OK
    json_response = response.json()
    assert "createdAt" in json_response
    assert "modifiedAt" in json_response
    assert json_response["title"] == "Bar"

    async with AsyncClient(app=app, base_url=base_url) as client:
        response = await client.get("/products")
    assert response.status_code == status.HTTP_200_OK
    expected_results = [{"title": "Foo"}, {"title": "Bar"}]
    products_from_response = response.json()["products"]

    for index, product_from_response in enumerate(products_from_response):
        assert product_from_response["title"] == expected_results[index]["title"]
