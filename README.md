Юнит-тесты для сервиса Stellar Burgers


Реализованы проверки методов класса burger:
1. Инициализация бургера - __init__
2. Установка булочки - set_buns
3. Добавление ингредиентов - add_ingredient
4. Удаление ингредиентов - remove_ingredient
5. Перемещение ингредиентов - move_ingredient
6. Расчёт стоимости бургера - get_price
7. Формирование чека - get_receipt


Структура проекта:
- tests/: файл с тестами для класс burger - test_burger.py
- файлы исходного кода: bun/burger/database/ingredient_types/ingredient/praktikum.py
- .gitignore: файл для исключения файлов из Git


Стек: Python 3.14.4, pytest, pytest-cov


Покрытие кода класса burger:

Name        Stmts   Miss  Cover   Missing
-----------------------------------------
burger.py      27      0   100%
-----------------------------------------
TOTAL          27      0   100%
