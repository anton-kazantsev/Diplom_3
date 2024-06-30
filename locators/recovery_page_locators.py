from selenium.webdriver.common.by import By


class RecoveryPageLocators:
    # ссылка Восстановить пароль
    RECOVERY_PASSWORD = [By.XPATH, ".//a[text()='Восстановить пароль']"]
    RECOVERY_PASSWORD_CLASS = [By.CLASS_NAME, "Auth_link__1fOlj"]

    # окно ввода почты для восстановления пароля
    RECOVERY_INPUT_EMAIL = [By.XPATH, ".//label[text()='Email']/../input[@type='text' and @name='name']"]
    # кнопка Восстановить
    RECOVERY_BUTTON = [By.XPATH, ".//button[text()='Восстановить']"]

    # окно ввода нового пароля
    RECOVERY_INPUT_NEW_PASSWORD = [By.XPATH, ".//label[text()='Пароль']/../"
                                             "input[@type='password' and @name='Введите новый пароль']"]
    RECOVERY_NEW_PASSWORD_VISIBLE = [By.XPATH, ".//label[text()='Пароль']/../"
                                             "input[@type='text' and @name='Введите новый пароль']"]
    # включение/выключение видимости пароля
    VISIBLE_BUTTON = [By.XPATH, ".//div[@class='input__icon input__icon-action']"]
