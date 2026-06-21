import random
import string

class RegistrationData:
    @staticmethod
    def generate_unique_email():
        random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        return f"test_{random_string}@example.com"

    @staticmethod
    def generate_unique_name():
        names = ["Alex", "Иван", "Mary", "Алексей", "Роман", "Дмитрий", "Катя", "Сергей"]
        random_name = random.choice(names)
        random_number = random.randint(100, 999)
        return f"{random_name}{random_number}"

    @staticmethod
    def generate_strong_password():
        chars = string.ascii_letters + string.digits
        return ''.join(random.choices(chars, k=10))

    valid_email = generate_unique_email.__func__()
    valid_name = generate_unique_name.__func__()
    valid_password = generate_strong_password.__func__()

    invalid_email = "invalid-email"
    invalid_password = "123"

class Logindata:
    email = 'testroman48@mail.ru'
    password = '12345678'
