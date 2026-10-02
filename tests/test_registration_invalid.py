from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import Locators


def test_registration_invalid_password(driver):
    driver.get("https://stellarburgers.education-services.ru/register")

    driver.find_element(*Locators.NAME_INPUT).send_keys("Тест Тестов")
    driver.find_element(*Locators.EMAIL_INPUT).send_keys("test_testov_42_123@yandex.ru")
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys("1")

    driver.find_element(*Locators.REGISTER_BUTTON).click()

    error = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(Locators.INVALID_PASSWORD_ERROR)
    )

    assert error.text == "Некорректный пароль"