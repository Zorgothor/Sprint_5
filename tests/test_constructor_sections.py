from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from generators import generate_registration_data
from locators import Locators


def test_constructor_sections(driver):
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

    # Ждём загрузки конструктора
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(Locators.SAUCES)
    )

    # Переходим в «Соусы»
    sauces = driver.find_element(*Locators.SAUCES)
    ActionChains(driver).move_to_element(sauces).click().perform()

    # Переходим в «Начинки»
    fillings = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(Locators.FILLINGS)
    )
    ActionChains(driver).move_to_element(fillings).click().perform()

    # Возвращаемся в «Булки»
    buns = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(Locators.BUNS)
    )
    ActionChains(driver).move_to_element(buns).click().perform()

    # Проверяем, что все разделы отображаются
    assert driver.find_element(*Locators.BUNS).is_displayed()
    assert driver.find_element(*Locators.SAUCES).is_displayed()
    assert driver.find_element(*Locators.FILLINGS).is_displayed()