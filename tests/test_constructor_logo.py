from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from generators import generate_registration_data
from locators import Locators


def test_constructor_from_logo(driver):
    driver.get("https://stellarburgers.education-services.ru/register")

    name, email, password = generate_registration_data()

    # Регистрируем нового пользователя
    driver.find_element(*Locators.NAME_INPUT).send_keys(name)
    driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*Locators.REGISTER_BUTTON).click()

    # Переходим на страницу входа
    driver.get("https://stellarburgers.education-services.ru/login")

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

    # Ждём открытия личного кабинета
    WebDriverWait(driver, 10).until(
        EC.url_contains("/account")
    )

    # Ждём исчезновения модального overlay
    WebDriverWait(driver, 10).until(
        EC.invisibility_of_element_located(
            (Locators.CONSTRUCTOR_LOGO[0], ".Modal_modal_overlay__x2ZCr")
        )
    )

    # Нажимаем на логотип Stellar Burgers
    driver.find_element(*Locators.CONSTRUCTOR_LOGO).click()

    # Проверяем переход в конструктор
    WebDriverWait(driver, 10).until(
        EC.url_to_be("https://stellarburgers.education-services.ru/")
    )

    assert driver.current_url == "https://stellarburgers.education-services.ru/"