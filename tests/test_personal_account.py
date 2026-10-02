from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from generators import generate_registration_data
from locators import Locators


def test_personal_account(driver):
    driver.get("https://stellarburgers.education-services.ru/register")

    name, email, password = generate_registration_data()

    # Регистрируем нового пользователя
    driver.find_element(*Locators.NAME_INPUT).send_keys(name)
    driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*Locators.REGISTER_BUTTON).click()

    WebDriverWait(driver, 10).until(
        EC.url_contains("/login")
    )

    # Входим в аккаунт
    driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*Locators.LOGIN_SUBMIT).click()

    # Ждём успешного входа
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(Locators.PERSONAL_ACCOUNT)
    )

    # Переходим в личный кабинет
    driver.find_element(*Locators.PERSONAL_ACCOUNT).click()

    # Проверяем, что открылась страница личного кабинета
    WebDriverWait(driver, 10).until(
        EC.url_contains("/account")
    )

    assert "/account" in driver.current_url