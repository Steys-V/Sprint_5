import random
import string
import time


def generate_email(domain="test.ru"):
    """
    Генерирует уникальный email для тестов.

    Формат: user_<случайные_символы>_<timestamp>@<domain>

    Пример: user_a3k9m2_1720785600@test.ru

    Args:
        domain (str): Домен email (по умолчанию "test.ru")

    Returns:
        str: Уникальный email
    """
    # Генерируем случайную строку из 6 символов
    random_str = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))

    # Добавляем timestamp для уникальности
    timestamp = int(time.time())

    # Формируем email
    email = f"user_{random_str}_{timestamp}@{domain}"

    return email


def generate_password(length=10):
    """
    Генерирует случайный пароль.

    Args:
        length (int): Длина пароля (по умолчанию 10)

    Returns:
        str: Случайный пароль
    """
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    password = ''.join(random.choices(characters, k=length))
    return password


def generate_name():
    """
    Генерирует случайное имя для регистрации.

    Returns:
        str: Случайное имя
    """
    names = ["Анна", "Иван", "Мария", "Пётр", "Елена", "Дмитрий", "Ольга", "Алексей"]
    return random.choice(names)