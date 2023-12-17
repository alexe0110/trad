from random import randint

from httpx import AsyncClient


async def test_add_operation(as_client: AsyncClient):
    response = await as_client.post(
        "/operations/",
        json={
            "id": randint(1, 99999),
            "quantity": "string",
            "figi": "12345",
            "instrument_type": "kek",
            "date": "2023-12-17T12:41:05.118",
            "type": "Покупка",
        },
    )
    assert response.status_code == 200


async def test_get_operations(as_client: AsyncClient):
    response = await as_client.get("/operations/", params={"operation_type": "kek"})
    assert response.status_code == 200
    assert response.json() == [], "операция kek существует"
