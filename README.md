
[📕 FastAPIUsers](https://fastapi-users.github.io/fastapi-users/10.0/)

## Подготовка окружения
    make init
    docker-compose up -d redis db    
    alembic upgrade head
или

    make init
    make up-db

## Запуск 
    export SMTP_USER=<адрес почты>
    export SMTP_PASS=<токен почты>

    source .venv/bin/activate
    uvicorn main:app --reload


## Тесты и Линтеры

#### Линтеры

    make pretty

#### ~~Tavern тесты~~ - пока не работает
    tavern-ci tests/tavern --alluredir=/tmp/allure --clean-alluredir

#### Pytest тесты
для тестов используется отдельная БД, на 6000 порту

    pytest -sv tests/



## Использование

#### Регистрация

#### Рандомные данные
https://www.coderstool.com/sql-test-data-generator

    INSERT INTO operation
    VALUES ('1', '23', 'QWER12', 'bond', '2022-04-10 09:18:10', 'Coupons');



Добавить роли 
```sql
insert into role values (1, 'user', null), (2, 'admin', null);
```
POST /auth/register
```json
{
  "email": "kek@gmail.com",
  "password": "mypass",
  "is_active": true,
  "is_superuser": false,
  "is_verified": false,
  "username": "kekUser",
  "role_id": 1
}
```

#### Celery
Чтобы развернуть Celery

	celery -A src.tasks.tasks.celery worker -D
    celery -A src.tasks.tasks.celery flower

или

    make celery-start

чтобы оставновить воркер

    make celery-stop