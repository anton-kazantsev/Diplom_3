import pytest
import allure
from conftest import driver
from conftest import generated_user_data
from conftest import generated_user_register
from conftest import generated_user_login
from conftest import generated_user_delete
from page_objects.order_feed_page import OrderFeedPage
from locators.base_page_locators import BasePageLocators
from locators.order_feed_page_locators import OrderFeedPageLocators
from locators.account_page_locators import AccountPageLocators
from locators.main_page_locators import MainPageLocators
from data import DataUrl


class TestOrderFeedPage:

    @allure.title('Всплывающее окно с деталями заказа')
    def test_order_feed_page_open_order(self, driver):
        feed_page = OrderFeedPage(driver)
        feed_page.click_element_and_waiting_element_download(BasePageLocators.ORDER_FEED,
                                                             OrderFeedPageLocators.LAST_ORDER)
        top_order_in_feed = feed_page.text_element(OrderFeedPageLocators.LAST_ORDER_NUMBER)
        feed_page.click_element_and_waiting_element_download(OrderFeedPageLocators.LAST_ORDER,
                                                             OrderFeedPageLocators.WINDOW_ORDER)
        order_in_modal = feed_page.text_element(OrderFeedPageLocators.ORDER_NUMBER_IN_MODAL)

        assert top_order_in_feed == order_in_modal

    @allure.title('Заказы пользователя из раздела История заказов отображаются в Ленте заказов')
    def test_order_feed_order_in_history_exists_in_feed(self, driver, generated_user_data, generated_user_register,
                                                        generated_user_login, generated_user_delete):
        feed_page = OrderFeedPage(driver)
        order_number = feed_page.place_order_get_number(MainPageLocators.BUN_LINK,
                                                        MainPageLocators.LINK_FILLING)
        feed_page.click_element_and_waiting_element_download(BasePageLocators.ORDER_FEED,
                                                             OrderFeedPageLocators.LAST_ORDER)
        is_order_in_feed = feed_page.is_displayed_order_in_feed(order_number)
        feed_page.click_element_and_waiting_element_download(BasePageLocators.BUTTON_ACCOUNT_HEADER,
                                                             AccountPageLocators.BUTTON_ORDER_HISTORY)
        feed_page.click_element_and_waiting_element_download(AccountPageLocators.BUTTON_ORDER_HISTORY,
                                                             AccountPageLocators.ORDER_HISTORY_LIST)
        is_order_in_history = feed_page.is_displayed_order_in_history(order_number)

        assert is_order_in_feed and is_order_in_history

    @allure.title('Увеличение счетчиков Выполнено за все время и Выполнено за сегодня при создании нового заказа')
    @pytest.mark.parametrize('counter', [OrderFeedPageLocators.COUNTER_ALL,
                                         OrderFeedPageLocators.COUNTER_TODAY])
    def test_order_feed_page_counters_growth(self, driver, generated_user_data, generated_user_register,
                                             generated_user_login, generated_user_delete, counter):
        feed_page = OrderFeedPage(driver)
        feed_page.click_element_and_waiting_element_download(BasePageLocators.ORDER_FEED, counter)
        counter_before = feed_page.text_element(counter)
        feed_page.open_page_and_waiting_element_download(DataUrl.MAIN_PAGE, MainPageLocators.BUN_LINK)
        order_number = feed_page.place_order_get_number(MainPageLocators.BUN_LINK,
                                                        MainPageLocators.LINK_FILLING)
        feed_page.click_element_and_waiting_element_download(BasePageLocators.ORDER_FEED, counter)
        feed_page.wait_element(OrderFeedPageLocators.STATUS_ORDER)
        order_number_in_in_process_box = OrderFeedPage.order_number_in_in_process_box_element(order_number)
        feed_page.wait_order_in_box(order_number_in_in_process_box)
        order_number_in_ready_box = OrderFeedPage.order_number_in_ready_box_element(order_number)
        feed_page.wait_order_in_box(order_number_in_ready_box)
        counter_after = feed_page.text_element(counter)

        assert counter_after > counter_before

    @allure.title('После оформления заказа его номер появляется в разделе В работе')
    def test_order_feed_page_order_number_in_status_box(self, driver, generated_user_data, generated_user_register,
                                                        generated_user_login, generated_user_delete):
        feed_page = OrderFeedPage(driver)
        order_number = feed_page.place_order_get_number(MainPageLocators.BUN_LINK,
                                                        MainPageLocators.LINK_FILLING)
        feed_page.click_element_and_waiting_element_download(BasePageLocators.ORDER_FEED,
                                                             OrderFeedPageLocators.STATUS_ORDER)
        order_number_in_in_process_box = OrderFeedPage.order_number_in_in_process_box_element(order_number)
        feed_page.wait_order_in_box(order_number_in_in_process_box)

        assert feed_page.is_displayed_order_in_status_box_in_process(order_number)
