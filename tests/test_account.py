import allure
from conftest import driver
from conftest import generated_user_data
from conftest import generated_user_register
from conftest import generated_user_login
from conftest import generated_user_delete
from page_objects.account_page import AccountPage
from locators.base_page_locators import BasePageLocators
from locators.account_page_locators import AccountPageLocators
from data import DataUrl


class TestAccount:

    @allure.title('Переход в личный кабинет через хэдер без авторизации')
    def test_account_page_open_not_authorized(self, driver):
        account_page = AccountPage(driver)
        account_page.wait_element(BasePageLocators.BUTTON_ACCOUNT_HEADER)
        account_page.click_element_and_waiting_element_download(BasePageLocators.BUTTON_ACCOUNT_HEADER,
                                                                AccountPageLocators.LOGIN_PAGE_HEADER)

        assert account_page.get_url() == DataUrl.LOGIN_PAGE

    @allure.title('Переход в личный кабинет через хэдер с авторизацией')
    def test_account_page_open_authorized(self, driver, generated_user_data, generated_user_register,
                                          generated_user_login, generated_user_delete):
        account_page = AccountPage(driver)
        account_page.wait_element(BasePageLocators.BUTTON_ACCOUNT_HEADER)
        account_page.click_element_and_waiting_element_download(BasePageLocators.BUTTON_ACCOUNT_HEADER,
                                                                AccountPageLocators.BUTTON_ORDER_HISTORY)

        assert account_page.get_url() == DataUrl.PROFILE_PAGE

    @allure.title('Переход в Историю заказов')
    def test_account_open_order_history(self, driver, generated_user_data, generated_user_register,
                                        generated_user_login, generated_user_delete):
        account_page = AccountPage(driver)
        account_page.two_clicks(BasePageLocators.BUTTON_ACCOUNT_HEADER, AccountPageLocators.BUTTON_ORDER_HISTORY,
                                AccountPageLocators.BUTTON_ORDER_HISTORY)

        assert account_page.get_url() == DataUrl.ORDER_HISTORY_PAGE

    @allure.title('Выход из аккаунта')
    def test_account_logout(self, driver, generated_user_data, generated_user_register,
                            generated_user_login, generated_user_delete):
        account_page = AccountPage(driver)
        account_page.two_clicks(BasePageLocators.BUTTON_ACCOUNT_HEADER, AccountPageLocators.BUTTON_OUT,
                                AccountPageLocators.LOGIN_PAGE_HEADER)

        assert account_page.get_url() == DataUrl.LOGIN_PAGE
