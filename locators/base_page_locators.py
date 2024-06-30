from selenium.webdriver.common.by import By


class BasePageLocators:
    # лого stellar burger
    LOGO_STELLAR_BURGER = [By.XPATH, ".//div[contains(@class, 'AppHeader_header__logo')]/a[@href='/']"]
    # вход в личный кабинет через хэдер
    BUTTON_ACCOUNT_HEADER = [By.XPATH,
                             ".//p[contains(@class, 'AppHeader_header__link') and text()='Личный Кабинет']/parent::a"]
    # открытие конструктора через хэдер
    CONSTRUCTOR_BUTTON = [By.XPATH,
                          ".//p[contains(@class, 'AppHeader_header__link') and text()='Конструктор']/parent::a"]
    # открытие ленты заказов через хэдер
    ORDER_FEED = [By.XPATH, ".//p[contains(@class, 'AppHeader_header__link') and text()='Лента Заказов']/parent::a"]
    # кнопка оформить заказ
    CHECKOUT_BUTTON = [By.XPATH, ".//div[contains(@class, 'BurgerConstructor_basket__container')]/button"]
    # область конструктора бургера
    BURGER_DESIGN = [By.XPATH, ".//ul[contains(@class, 'BurgerConstructor_basket')]"]
    # кнопка закрытия деталей ингредиента
    BUTTON_CLOSE_INGREDIENT = [By.XPATH, ".//button[contains(@class, 'Modal_modal__close')]"]
    # номер нового заказа
    NEW_ORDER_NUMBER = [By.XPATH, ".//section[contains(@class, 'modal_opened')]//"
                                           "div[contains(@class, 'Modal_modal__contentBox')]/"
                                           "h2[contains(@class, 'text_type_digits-large')]"]
