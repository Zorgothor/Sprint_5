from selenium.webdriver.common.by import By


class Locators:

    # Ссылка «Личный кабинет» в шапке сайта
    PERSONAL_ACCOUNT = (By.CSS_SELECTOR, 'a[href="/account"]')

    # Кнопка «Войти в аккаунт» на главной странице
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")

    # Ссылка «Конструктор» в шапке сайта
    CONSTRUCTOR = (By.XPATH, "//p[text()='Конструктор']")

    # Логотип Stellar Burgers в шапке сайта
    CONSTRUCTOR_LOGO = (By.CSS_SELECTOR, 'a[href="/"] svg')

    # Кнопка «Войти» на странице авторизации
    LOGIN_SUBMIT = (By.XPATH, "//button[text()='Войти']")

    # Поле «Имя» на странице регистрации
    NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")

    # Поле «Email» на страницах регистрации и авторизации
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")

    # Поле «Пароль» на страницах регистрации и авторизации
    PASSWORD_INPUT = (By.NAME, "Пароль")

    # Кнопка «Зарегистрироваться»
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")

    # Ссылка «Войти» в форме регистрации
    LOGIN_FROM_REGISTER = (By.CSS_SELECTOR, 'a[href="/login"]')

    # Ссылка «Восстановить пароль»
    FORGOT_PASSWORD = (By.CSS_SELECTOR, 'a[href="/forgot-password"]')

    # Сообщение о некорректном пароле
    INVALID_PASSWORD_ERROR = (By.CSS_SELECTOR, 'p.input__error')

    # Кнопка «Выход» в личном кабинете
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")

    # Вкладка «Булки» в конструкторе
    BUNS = (By.XPATH, "//div[span[text()='Булки']]")

    # Вкладка «Соусы» в конструкторе
    SAUCES = (By.XPATH, "//div[span[text()='Соусы']]")

    # Вкладка «Начинки» в конструкторе
    FILLINGS = (By.XPATH, "//div[span[text()='Начинки']]")

    # Модальный overlay
MODAL_OVERLAY = (By.CSS_SELECTOR, "div.Modal_modal_overlay__x2ZCr")