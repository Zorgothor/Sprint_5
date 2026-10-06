from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from constants import BASE_URL, REGISTER_URL, LOGIN_URL
from generators import generate_registration_data
from locators import Locators


class TestLogin:

    def test_login_from_main_page(self, driver):
        driver.get(REGISTER_URL)

        name, email, password = generate_registration_data()

        driver.find_element(*Locators.NAME_INPUT).send_keys(name)
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Locators.REGISTER_BUTTON).click()

        WebDriverWait(driver, 10).until(
            EC.url_contains("/login")
        )

        driver.get(BASE_URL)

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

    def test_login_from_recovery_form(self, driver):
        driver.get(REGISTER_URL)

        name, email, password = generate_registration_data()

        driver.find_element(*Locators.NAME_INPUT).send_keys(name)
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Locators.REGISTER_BUTTON).click()

        WebDriverWait(driver, 10).until(
            EC.url_contains("/login")
        )

        driver.get(f"{BASE_URL}/forgot-password")

        driver.find_element(*Locators.LOGIN_FROM_REGISTER).click()

        WebDriverWait(driver, 10).until(
            EC.url_contains("/login")
        )

        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Locators.LOGIN_SUBMIT).click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.PERSONAL_ACCOUNT)
        )

        assert driver.find_element(*Locators.PERSONAL_ACCOUNT).is_displayed()

    def test_login_from_registration_form(self, driver):
        driver.get(REGISTER_URL)

        name, email, password = generate_registration_data()

        driver.find_element(*Locators.NAME_INPUT).send_keys(name)
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Locators.REGISTER_BUTTON).click()

        WebDriverWait(driver, 10).until(
            EC.url_contains("/login")
        )

        driver.get(REGISTER_URL)

        driver.find_element(*Locators.LOGIN_FROM_REGISTER).click()

        WebDriverWait(driver, 10).until(
            EC.url_contains("/login")
        )

        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Locators.LOGIN_SUBMIT).click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.PERSONAL_ACCOUNT)
        )

        assert driver.find_element(*Locators.PERSONAL_ACCOUNT).is_displayed()

    def test_login_from_personal_account(self, driver):
        driver.get(REGISTER_URL)

        name, email, password = generate_registration_data()

        driver.find_element(*Locators.NAME_INPUT).send_keys(name)
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Locators.REGISTER_BUTTON).click()

        WebDriverWait(driver, 10).until(
            EC.url_contains("/login")
        )

        driver.get(BASE_URL)

        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()

        WebDriverWait(driver, 10).until(
            EC.url_contains("/login")
        )

        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Locators.LOGIN_SUBMIT).click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(Locators.PERSONAL_ACCOUNT)
        )

        assert driver.find_element(*Locators.PERSONAL_ACCOUNT).is_displayed()

    def test_logout(self, driver):
        driver.get(REGISTER_URL)

        name, email, password = generate_registration_data()

        driver.find_element(*Locators.NAME_INPUT).send_keys(name)
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Locators.REGISTER_BUTTON).click()

        driver.get(LOGIN_URL)

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

        driver.find_element(*Locators.LOGOUT_BUTTON).click()

        WebDriverWait(driver, 10).until(
            EC.url_contains("/login")
        )

        assert "/login" in driver.current_url