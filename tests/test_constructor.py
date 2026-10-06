from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from constants import BASE_URL, REGISTER_URL, LOGIN_URL
from generators import generate_registration_data
from locators import Locators


class TestConstructor:

    def test_constructor_from_account(self, driver):
        driver.get(REGISTER_URL)

        name, email, password = generate_registration_data()

        # Регистрируем нового пользователя
        driver.find_element(*Locators.NAME_INPUT).send_keys(name)
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Locators.REGISTER_BUTTON).click()

        # Переходим на страницу входа
        driver.get(LOGIN_URL)

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

        WebDriverWait(driver, 10).until(
            EC.url_contains("/account")
        )

        # Нажимаем «Конструктор»
        driver.find_element(*Locators.CONSTRUCTOR).click()

        # Проверяем переход в конструктор
        WebDriverWait(driver, 10).until(
            EC.url_to_be(BASE_URL + "/")
        )

        assert driver.current_url == BASE_URL + "/"

    def test_constructor_from_logo(self, driver):
        driver.get(REGISTER_URL)

        name, email, password = generate_registration_data()

        # Регистрируем нового пользователя
        driver.find_element(*Locators.NAME_INPUT).send_keys(name)
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Locators.REGISTER_BUTTON).click()

        # Переходим на страницу входа
        driver.get(LOGIN_URL)

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
            EC.url_to_be(BASE_URL + "/")
        )

        assert driver.current_url == BASE_URL + "/"

    def test_constructor_sections(self, driver):
        driver.get(REGISTER_URL)

        name, email, password = generate_registration_data()

        # Регистрируем нового пользователя
        driver.find_element(*Locators.NAME_INPUT).send_keys(name)
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Locators.REGISTER_BUTTON).click()

        # Переходим на страницу входа
        driver.get(LOGIN_URL)

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