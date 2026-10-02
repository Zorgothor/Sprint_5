from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from generators import generate_registration_data
from locators import Locators


def test_login_from_main_page(driver):
    driver.get("https://stellarburgers.education-services.ru/register")

    name, email, password = generate_registration_data()

    driver.find_element(*Locators.NAME_INPUT).send_keys(name)
    driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*Locators.REGISTER_BUTTON).click()

    WebDriverWait(driver, 10).until(
        EC.url_contains("/login")
    )

    driver.get("https://stellarburgers.education-services.ru/")

    driver.find_element(*Locators.LOGIN_BUTTON).click()

    WebDriverWait(driver, 10).until(
        EC.url_contains("/login")
    )

    driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*Locators.LOGIN_SUBMIT).click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(Locators.PERSONAL_ACCOUNT)
    )

    driver.find_element(*Locators.PERSONAL_ACCOUNT).click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(Locators.LOGOUT_BUTTON)
    )

    assert driver.find_element(*Locators.LOGOUT_BUTTON).is_displayed()