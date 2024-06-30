from selenium.webdriver.common.by import By


class OrderFeedPageLocators:
    # номера заказов в работе
    STATUS_ORDER = [By.XPATH, ".//ul[contains(@class, 'OrderFeed_orderListReady')]"]
    # последний заказ в ленте заказов
    LAST_ORDER = [By.XPATH, ".//ul[contains(@class, 'OrderFeed_list')]/li[1]/a"]
    # номер заказа в окне заказа
    ORDER_NUMBER_IN_MODAL = [By.XPATH, ".//section[contains(@class, 'modal_opened')]//"
                                       "div[contains(@class, 'Modal_modal__contentBox')]/"
                                       "p[contains(@class, 'text_type_digits-default')]"]
    # номер последнего заказа в ленте заказов
    LAST_ORDER_NUMBER = [By.XPATH, ".//ul[contains(@class, 'OrderFeed_list')]/li[1]//"
                                   "div[contains(@class, 'OrderHistory_textBox')]"
                                   "/p[contains(@class, 'text_type_digits-default')]"]

    # окно заказа
    WINDOW_ORDER = [By.XPATH, ".//section[contains(@class, 'modal_opened')]"]
    # номер заказа в окне заказа
    NUMBER_NEW_ORDER = [By.XPATH, ".//section[contains(@class, 'modal_opened')]//"
                                           "div[contains(@class, 'Modal_modal__contentBox')]/"
                                           "h2[contains(@class, 'text_type_digits-large')]"]
    # анимация готового заказа
    GIF_READY = [By.XPATH, ".//img[@src='./static/media/tick.887b83be.gif']"]

    # счетчик выполненных заказов за все время
    COUNTER_ALL = [By.XPATH, ".//p[text()='Выполнено за все время:']/../p[contains(@class, 'OrderFeed_number')]"]
    # счетчик выполненных заказов за сегодня
    COUNTER_TODAY = [By.XPATH, ".//p[text()='Выполнено за сегодня:']/../p[contains(@class, 'OrderFeed_number')]"]

