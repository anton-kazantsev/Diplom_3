import allure
import string
import random
import pytest
import requests
import data
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.base_page_locators import BasePageLocators
from locators.account_page_locators import AccountPageLocators


@allure.step("Запустить браузер. Перейти на главную страницу Stellar Burgers. "
             " ернуть тип браузера. Закрыть браузер по завершении теста")
@pytest.fixture(params=['firefox', 'chrome'], scope='function')
def driver(request):
    driver = None

    if request.param == 'firefox':
        driver = webdriver.Firefox()
    elif request.param == 'chrome':
        driver = webdriver.Chrome()

    driver.get(data.DataUrl.MAIN_PAGE)

    yield driver

    driver.quit()


@allure.step("Авторизоваться. Дождаться перехода на главную страницу.")
@pytest.fixture(scope='function')
def generated_user_login(driver, generated_user_register):

    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(BasePageLocators.BUTTON_ACCOUNT_HEADER))
    driver.execute_script("arguments[0].click();", driver.find_element(*BasePageLocators.BUTTON_ACCOUNT_HEADER))
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(AccountPageLocators.LOGIN_EMAIL))
    driver.find_element(*AccountPageLocators.LOGIN_EMAIL).send_keys(generated_user_register['email'])
    driver.find_element(*AccountPageLocators.LOGIN_PASSWORD).send_keys(generated_user_register['password'])
    driver.execute_script("arguments[0].click();", driver.find_element(*AccountPageLocators.BUTTON_IN))
    WebDriverWait(driver, 5).until(expected_conditions.url_to_be(data.DataUrl.MAIN_PAGE))


@allure.step("Удалить рандомного пользователя по завершении теста")
@pytest.fixture(scope='function')
def generated_user_delete(driver, generated_user_register):

    yield

    headers = dict(Authorization=generated_user_register['token'])
    wait_ten = 0
    while wait_ten != 10:
        response = requests.delete(data.DataUrl.USER_AUTHORIZATION_PAGE, headers=headers)
        wait_ten += 1 if response.status_code != 202 else 10


@allure.step('Генерация рандомных учетных данных для регистрации нового пользователя. Вернуть данные.')
@pytest.fixture(scope='function')
def generated_user_data():

    def random_email():
        return 'antonkazantcev' + ''.join(random.choice(string.ascii_letters) for _ in range(5)) + "@yandex.ru"

    def random_password():
        return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(12))

    email = random_email()
    password = random_password()
    name = 'Антон'

    random_body = {
        "email": email,
        "password": password,
        "name": name
    }

    return random_body


@allure.step('Зарегистрировать нового рандомного пользователя. Вернуть учетные данные и токен авторизации')
@pytest.fixture(scope='function')
def generated_user_register(generated_user_data):
    wait_ten = 0
    while wait_ten != 10:
        response = requests.post(data.DataUrl.USER_REGISTER_PAGE, json=generated_user_data)
        wait_ten += 1 if response.status_code != 200 else 10
    generated_user_data['token'] = response.json()["accessToken"]

    return generated_user_data
