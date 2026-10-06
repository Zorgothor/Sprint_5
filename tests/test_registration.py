from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from constants import REGISTER_URL
from generators import generate_registration_data
from locators import Locators


class TestRegistration:

    def test_successful_registration(self, driver):
        driver.get(REGISTER_URL)

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

    def test_registration_invalid_password(self, driver):
        driver.get(REGISTER_URL)

        driver.find_element(*Locators.NAME_INPUT).send_keys("Тест Тестов")
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(
            "test_testov_42_123@yandex.ru"
        )
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys("1")

        driver.find_element(*Locators.REGISTER_BUTTON).click()

        error = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.INVALID_PASSWORD_ERROR)
        )

        assert error.text == "Некорректный пароль"