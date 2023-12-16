import pytest


@pytest.fixture
def clear_trades(request):
    print("Перед фикстурой")
    # TRADES.clear()
    print("После фикстуры")
