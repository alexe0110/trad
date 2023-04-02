from fastapi import FastAPI

app = FastAPI(
    title="Trading App"
)


@app.get("/")
def hello(name: str):
    return f"Hello, {name}"


fake_users = [
    {"id": 1, "role": "admin", "name": "Bob"},
    {"id": 2, "role": "investor", "name": "John"},
    {"id": 3, "role": "trader", "name": "Matt"},
]

fake_trades = [
    {"id": 1, "user_id": 1, "currency": "BTC", "side": "buy", "price": 123, "amount": 2.12},
    {"id": 2, "user_id": 1, "currency": "BTC", "side": "sell", "price": 125, "amount": 2.12},
]


@app.get("/user/{user_id}")
def get_user(user_id: int):
    return [user for user in fake_users if user.get("id") == user_id]


@app.get("/trades")
def get_trades(limit: int = 1, offset: int = 0):
    return fake_trades[offset:][:limit]