from selenium.webdriver.common.by import By


class AccountPageLocators:
    # заголовок Вход
    LOGIN_PAGE_HEADER = [By.XPATH, ".//h2[text()='Вход']"]

    # поле ввода email
    LOGIN_EMAIL = [By.XPATH, ".//div[contains(@class, 'Auth_login')]//label[text()='Email']/../input[@name='name']"]
    # поле ввода пароля
    LOGIN_PASSWORD = [By.XPATH,
                      ".//div[contains(@class, 'Auth_login')]//label[text()='Пароль']/../input[@name='Пароль']"]
    # кнопка Войти
    BUTTON_IN = [By.XPATH, ".//button[text()='Войти']"]
    # кнопка оформить заказ
    ORDER_BUTTON = [By.XPATH, './/button[text() = "Оформить заказ"]']
    # кнопка выхода из аккаунта
    BUTTON_OUT = [By.XPATH, ".//button[text()='Выход']"]

    # история заказов
    BUTTON_ORDER_HISTORY = [By.XPATH, ".//a[text()='История заказов']"]
    # выполненный заказ
    ORDER_HISTORY_LIST = [By.XPATH,
                          ".//div[contains(@class, 'Account_contentBox')]//ul[contains(@class, 'OrderHistory_list')]"]
    # список выполненных заказов
    ORDER_HISTORY = [By.XPATH, ".//div[contains(@class, 'OrderHistory_orderHistory')]"]
