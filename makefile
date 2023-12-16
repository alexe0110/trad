VENV ?= .venv
PYTHON_VERSION := 3.11
CODE = src tests

init:
	python$(PYTHON_VERSION) -m venv $(VENV)
	$(VENV)/bin/python -m pip install --upgrade pip
	$(VENV)/bin/python -m pip install poetry
	$(VENV)/bin/poetry install

up-db:
	docker-compose up -d redis db
	alembic upgrade head

pretty:
	$(VENV)/bin/isort $(CODE)
	$(VENV)/bin/black $(CODE)