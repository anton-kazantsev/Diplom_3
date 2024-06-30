from selenium.webdriver.common.by import By


class MainPageLocators:
    # текст Соберите бургер
    CONSTRUCTOR = [By.XPATH, ".//h1[text()='Соберите бургер']"]
    # текст Лента заказов в хэдере
    ORDER_FEED = [By.XPATH, ".//h1[text()='Лента заказов']"]

    # ссылка на начинку
    LINK_FILLING = [By.XPATH, ".//a[@href='/ingredient/61c0c5a71d1f82001bdaaa6e']"]
    # счетчик количества добавленной начинки
    FILLING_COUNTER = [By.XPATH, ".//a[@href='/ingredient/61c0c5a71d1f82001bdaaa6e']//p[contains(@class, 'counter')]"]
    # ссылка на булку
    BUN_LINK = [By.XPATH, ".//a[@href='/ingredient/61c0c5a71d1f82001bdaaa6c']"]

    # заголовок окна Детали ингредиента
    DETAILS_HEADER = [By.XPATH, ".//h2[text()='Детали ингредиента']"]
    # кнопка закрытия окна деталей ингредиента
    BUTTON_CLOSE_DETAILS = [By.XPATH, ".//button[contains(@class, 'Modal_modal__close')]"]
    # открытое окно деталей ингредиента
    OPEN_DETAILS = [By.XPATH, ".//section[contains(@class, 'modal_opened')]"]

    # окно сборки бургера
    BURGER_ASSEMBLY = [By.XPATH, ".//ul[contains(@class, 'BurgerConstructor_basket')]"]
    # кнопка оформления заказа
    MAKING_ORDER = [By.XPATH, ".//div[contains(@class, 'BurgerConstructor_basket__container')]/button"]

    # номер заказа
    ORDER_ID = [By.XPATH, ".//p[text()='идентификатор заказа']/../h2"]