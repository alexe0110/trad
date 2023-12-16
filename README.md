
[📕 FastAPIUsers](https://fastapi-users.github.io/fastapi-users/10.0/)

#### Подготовка окружения
    make init
    docker-compose up -d redis db    
    alembic upgrade head
или

    make init
    make up-db

#### Запуск 
    source .venv/bin/activate
    uvicorn main:app --reload


#### ~~Tavern тесты пока не работает~~ 
    tavern-ci tests/tavern --alluredir=/tmp/allure --clean-alluredir


#### Рандомные данные
https://www.coderstool.com/sql-test-data-generator

    INSERT INTO operation
    VALUES ('1', '23', 'QWER12', 'bond', '2022-04-10 09:18:10', 'Coupons');


### Использование 


##### Регистрация
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