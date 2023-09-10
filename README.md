

#### Запуск 

    source .venv/bin/activate
    uvicorn main:app --reload


#### Tavern тесты
    tavern-ci tests/tavern --alluredir=/tmp/allure --clean-alluredir


#### Рандомные данные
https://www.coderstool.com/sql-test-data-generator

    INSERT INTO operation
    VALUES ('1', '23', 'QWER12', 'bond', '2022-04-10 09:18:10', 'Coupons');