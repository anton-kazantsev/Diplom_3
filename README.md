## Дипломный проект. Задание 3: веб-приложение

### Автотесты проверки веб-приложения Stellar Burgers

### Реализованные сценарии

Созданы локаторы и POM для выполнения тестов

Восстановление пароля:
- переход на страницу восстановления пароля по кнопке «Восстановить пароль»,
- ввод почты и клик по кнопке «Восстановить»,
- клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его.
Тесты:
- test_recovery_password

Личный кабинет:
- переход по клику на «Личный кабинет»,
- переход в раздел «История заказов»,
- выход из аккаунта.
Тесты:
- test_account

Проверка основного функционала:
- переход по клику на «Конструктор»,
- переход по клику на «Лента заказов»,
- если кликнуть на ингредиент, появится всплывающее окно с деталями,
- всплывающее окно закрывается кликом по крестику,
- при добавлении ингредиента в заказ счётчик этого ингридиента увеличивается,
- залогиненный пользователь может оформить заказ.
Тесты:
- test_main_function

Раздел «Лента заказов»:
- если кликнуть на заказ, откроется всплывающее окно с деталями,
- заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»,
- при создании нового заказа счётчик Выполнено за всё время увеличивается,
- при создании нового заказа счётчик Выполнено за сегодня увеличивается,
- после оформления заказа его номер появляется в разделе В работе.
Тесты:
- test_order_feed

### Структура проекта

- `allure_results` - отчет о тестировании
- `tests` - пакет, содержащий тесты, разделенные по классам.
- `page_objects` - пакет, содержащий объекты тестируемых страниц веб-приложения
- `locators` - пакет, содержащий локаторы объектов страниц в соответсвии с POM

### Запуск автотестов

**Установка зависимостей**

> `$ pip3 install -r requirements.txt`

**Запуск автотестов и создание отчета о тестировании**

>  `$ pytest --alluredir=allure_results`

**Просмотр отчета о тестировании**

>  `$ allure serve allure_results`
