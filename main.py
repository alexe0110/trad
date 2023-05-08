from typing import List

from fastapi import FastAPI
from http import HTTPStatus

from starlette.responses import JSONResponse
from data import USERS, TRADES
from models import Trade, User

app = FastAPI(
    title="Trading App"
)


@app.get("/")
def hello(name: str):
    return JSONResponse(
        status_code=HTTPStatus.OK,
        content={
            "message": "Hello, " + name
        },
    )


@app.get("/user/{user_id}", response_model=list[User])
def get_user(user_id: int):
    return [user for user in USERS if user.get("id") == user_id]


@app.post("/user/{user_id}")
def post_change_name(user_id: int, new_name: str):
    current_user = list(filter(lambda user: user.get("id") == user_id, USERS))[0]
    current_user["name"] = new_name
    return {"status": HTTPStatus.OK, "new name": current_user}


@app.get("/trades")
def get_trades():
    return TRADES


@app.post("/trades")
def add_trades(trades: List[Trade]):
    TRADES.extend(trades)
    return {"status": HTTPStatus.OK, "data": TRADES}
