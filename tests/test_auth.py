from fastapi.testclient import TestClient
from sqlalchemy import insert, select

from src.auth.models import role


async def test_register(as_client: TestClient, db_session):
    smtp = insert(role).values(id=1, name="admin", permissions=None)
    await db_session.execute(smtp)
    await db_session.commit()

    response = await as_client.post(
        "/auth/register",
        json={
            "email": "test_user",
            "password": "test_user",
            "is_active": True,
            "is_superuser": False,
            "is_verified": False,
            "username": "user",
            "role_id": 1,
        },
    )
    assert response.status_code == 201
