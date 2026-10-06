import random
import string


def generate_registration_data():
    number = random.randint(100, 999)

    password = (
        random.choice(string.ascii_uppercase)
        + random.choice(string.ascii_lowercase)
        + random.choice(string.digits)
        + random.choice("!@#$%^&*")
        + ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    )

    email = f"test_testov_42_{number}@yandex.ru"

    return "Тест Тестов", email, password