from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from generators import generate_registration_data
from locators import Locators


def test_successful_registration(driver):
    driver.get("https://stellarburgers.education-services.ru/register")

    name, email, password = generate_registration_data()

    driver.find_element(*Locators.NAME_INPUT).send_keys(name)
    driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(Locators.REGISTER_BUTTON)
    ).click()

    WebDriverWait(driver, 10).until(
        EC.url_contains("/login")
    )