import pytest
from sqlalchemy import insert, select

from src.auth.models import role


async def test_add_role(db_session):
    smtp = insert(role).values(id=1, name="admin", permissions=None)
    await db_session.execute(smtp)
    await db_session.commit()

    qwery = select(role)
    result = await db_session.execute(qwery)
    print(result.all())


def test_register(client):
    response = client.post(
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
