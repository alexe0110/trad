from typing import List

from fastapi import FastAPI, Depends
from http import HTTPStatus

from fastapi_users import FastAPIUsers
from auth.schemas import UserCreate, UserRead
from auth.auth import auth_backend
from auth.manager import get_user_manager
from auth.database import User


fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app = FastAPI(
    title="Trading App"
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

current_user = fastapi_users.current_user()


@app.get("/protected_route")
def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.username}"


@app.get("/unprotected_route")
def protected_route():
    return "Hello, kek"
