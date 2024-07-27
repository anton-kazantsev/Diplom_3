import allure
import data
from conftest import driver
from data import DataUrl
from page_objects.recovery_page import RecoveryPage
from locators.recovery_page_locators import RecoveryPageLocators


class TestRecoveryPassword:

    @allure.title('Переход на страницу восстановления пароля по ссылке Восстановить пароль')
    def test_recovery_page_open_from_login_page(self, driver):
        recovery_page = RecoveryPage(driver)
        recovery_page.open_page_and_waiting_element_download(DataUrl.LOGIN_PAGE,
                                                             RecoveryPageLocators.RECOVERY_PASSWORD)
        recovery_page.click_element_and_waiting_element_download(RecoveryPageLocators.RECOVERY_PASSWORD,
                                                                 RecoveryPageLocators.RECOVERY_INPUT_EMAIL)

        assert recovery_page.get_url() == DataUrl.RECOVERY_INPUT_EMAIL_PAGE

    @allure.title('Ввод почты и нажатие на кнопку Восстановить')
    def test_recovery_input_email_and_open_next_page(self, driver):
        recovery_page = RecoveryPage(driver)
        recovery_page.open_page_and_waiting_element_download(DataUrl.RECOVERY_INPUT_EMAIL_PAGE,
                                                             RecoveryPageLocators.RECOVERY_INPUT_EMAIL)
        recovery_page.set_value_click_button_and_wait(RecoveryPageLocators.RECOVERY_INPUT_EMAIL,
                                                      data.DataUser.EMAIL,
                                                      RecoveryPageLocators.RECOVERY_BUTTON,
                                                      RecoveryPageLocators.RECOVERY_INPUT_NEW_PASSWORD)

        assert recovery_page.get_url() == DataUrl.RECOVERY_INPUT_PASSWORD_PAGE

    @allure.title('Нажатие на кнопку показать/скрыть пароль делает поле активным')
    def test_recovery_password_visibility(self, driver):
        recovery_page = RecoveryPage(driver)
        recovery_page.open_page_and_waiting_element_download(DataUrl.RECOVERY_INPUT_EMAIL_PAGE,
                                                             RecoveryPageLocators.RECOVERY_INPUT_EMAIL)
        recovery_page.set_value_click_button_and_wait(RecoveryPageLocators.RECOVERY_INPUT_EMAIL,
                                                      data.DataUser.EMAIL,
                                                      RecoveryPageLocators.RECOVERY_BUTTON,
                                                      RecoveryPageLocators.RECOVERY_INPUT_NEW_PASSWORD)
        recovery_page.set_value_click_button_and_wait(RecoveryPageLocators.RECOVERY_INPUT_NEW_PASSWORD,
                                                      data.DataUser.PASSWORD,
                                                      RecoveryPageLocators.VISIBLE_BUTTON,
                                                      RecoveryPageLocators.RECOVERY_NEW_PASSWORD_VISIBLE)

        assert recovery_page.get_attribute(RecoveryPageLocators.RECOVERY_NEW_PASSWORD_VISIBLE, 'type') == 'text'
