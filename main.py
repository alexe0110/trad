from typing import List

from fastapi import FastAPI, Depends
from http import HTTPStatus

from starlette.responses import JSONResponse
from data import USERS, TRADES
# from models import Trade, User
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


# @app.get("/")
# def hello(name: str):
#     return JSONResponse(
#         status_code=HTTPStatus.OK,
#         content={
#             "message": "Hello, " + name
#         },
#     )
#
#
# @app.get("/user/{user_id}", response_model=list[User])
# def get_user(user_id: int):
#     return [user for user in USERS if user.get("id") == user_id]
#
#
# @app.post("/user/{user_id}")
# def post_change_name(user_id: int, new_name: str):
#     current_user = list(filter(lambda user: user.get("id") == user_id, USERS))[0]
#     current_user["name"] = new_name
#     return {"status": HTTPStatus.OK, "new name": current_user}
#
#
# @app.get("/trades")
# def get_trades():
#     return TRADES
#
#
# @app.post("/trades")
# def add_trades(trades: List[Trade]):
#     TRADES.extend(trades)
#     return {"status": HTTPStatus.OK, "data": TRADES}
