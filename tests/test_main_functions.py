import allure
from conftest import driver
from conftest import generated_user_data
from conftest import generated_user_register
from conftest import generated_user_login
from conftest import generated_user_delete
from page_objects.main_page import MainPage
from locators.base_page_locators import BasePageLocators
from locators.main_page_locators import MainPageLocators
from data import DataUrl


class TestMainPage:

    @allure.title('Переход в Конструктор')
    def test_main_page_open_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.open_page_and_waiting_element_download(DataUrl.LOGIN_PAGE, BasePageLocators.CONSTRUCTOR_BUTTON)
        main_page.click_element_and_waiting_element_download(BasePageLocators.CONSTRUCTOR_BUTTON,
                                                             MainPageLocators.CONSTRUCTOR)

        assert main_page.get_url() == DataUrl.MAIN_PAGE

    @allure.title('Переход в Ленту заказов')
    def test_main_page_open_feed(self, driver):
        main_page = MainPage(driver)
        main_page.wait_element(BasePageLocators.ORDER_FEED)
        main_page.click_element_and_waiting_element_download(BasePageLocators.ORDER_FEED,
                                                             MainPageLocators.ORDER_FEED)

        assert main_page.get_url() == DataUrl.FEED_PAGE

    @allure.title('Появление окна с деталями ингредиентов')
    def test_main_page_ingredient_details_modal(self, driver):
        main_page = MainPage(driver)
        main_page.wait_element(MainPageLocators.CONSTRUCTOR)
        main_page.scroll_page(MainPageLocators.LINK_FILLING)
        main_page.click_element_and_waiting_element_download(MainPageLocators.LINK_FILLING,
                                                             MainPageLocators.DETAILS_HEADER)

        assert main_page.get_url() == DataUrl.INGREDIENT_PAGE

    @allure.title('Закрытие деталей ингредиентов по нажатию на крестик')
    def test_main_page_ingredient_modal_close(self, driver):
        main_page = MainPage(driver)
        main_page.wait_element(MainPageLocators.CONSTRUCTOR)
        main_page.scroll_page(MainPageLocators.LINK_FILLING)
        main_page.click_element_and_waiting_element_download(MainPageLocators.LINK_FILLING,
                                                             MainPageLocators.OPEN_DETAILS)
        main_page.click_element_and_waiting_element_download(MainPageLocators.BUTTON_CLOSE_DETAILS,
                                                             MainPageLocators.CONSTRUCTOR)

        assert not main_page.is_elements_exist(MainPageLocators.OPEN_DETAILS)

    @allure.title('Увеличение счетчика ингредиентов, при добавлении их в заказ')
    def test_main_page_basket_counter_growth(self, driver):
        main_page = MainPage(driver)
        counter_before = main_page.counter_value(MainPageLocators.FILLING_COUNTER)
        main_page.add_ingredient_to_basket(MainPageLocators.LINK_FILLING)
        counter_after = main_page.counter_value(MainPageLocators.FILLING_COUNTER)

        assert counter_before < counter_after

    @allure.title('Оформление заказа зарегистрированным пользователем')
    def test_main_page_place_order_authorized_success(self, driver, generated_user_data, generated_user_register,
                                                      generated_user_login, generated_user_delete):
        main_page = MainPage(driver)
        order_id_before = main_page.text_element(MainPageLocators.ORDER_ID)
        main_page.add_ingredient_to_basket(MainPageLocators.BUN_LINK)
        main_page.add_ingredient_to_basket(MainPageLocators.LINK_FILLING)
        main_page.click_element_and_waiting_element_download(MainPageLocators.MAKING_ORDER,
                                                             MainPageLocators.ORDER_ID)
        order_id_after = main_page.text_element(MainPageLocators.ORDER_ID)

        assert order_id_after != order_id_before and main_page.is_elements_exist(MainPageLocators.OPEN_DETAILS)
