import pytest
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers import generate_email, generate_password
from locators import (
    BUTTON_LOGIN_MAIN,
    LINK_REGISTER,
    INPUT_NAME,
    INPUT_EMAIL_BY_LABEL,
    INPUT_PASSWORD,
    BUTTON_REGISTER,
    BUTTON_LOGIN,
    LINK_PERSONAL_ACCOUNT,
    TEXT_PERSONAL_ACCOUNT
)
from config import BASE_URL, ACCOUNT_URL, TIMEOUT_MEDIUM

# Настройка логгирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


@pytest.fixture
def driver():
    """Фикстура: создаёт и закрывает браузер"""
    browser = webdriver.Chrome()
    browser.implicitly_wait(TIMEOUT_MEDIUM)
    yield browser
    browser.quit()


@pytest.fixture
def test_credentials():
    """Фикстура: генерирует тестовые данные"""
    email = generate_email()
    password = generate_password()

    logger.info(f"Сгенерированы тестовые данные: email={email}")

    return {
        "email": email,
        "password": password,
        "name": "Тест"
    }


@pytest.fixture
def registered_user(driver, test_credentials):
    """
    Фикстура: регистрирует нового пользователя.

    Returns:
        dict: Данные пользователя (email, password, name)
    """
    driver.get(BASE_URL)

    # Переход на регистрацию
    driver.find_element(*BUTTON_LOGIN_MAIN).click()
    driver.find_element(*LINK_REGISTER).click()

    WebDriverWait(driver, TIMEOUT_MEDIUM).until(
        EC.visibility_of_element_located((By.NAME, "name"))
    )

    # Заполнение формы регистрации
    driver.find_element(*INPUT_NAME).send_keys(test_credentials["name"])
    driver.find_element(*INPUT_EMAIL_BY_LABEL).send_keys(test_credentials["email"])
    driver.find_element(*INPUT_PASSWORD).send_keys(test_credentials["password"])
    driver.find_element(*BUTTON_REGISTER).click()

    # Ожидание перехода на страницу входа
    WebDriverWait(driver, TIMEOUT_MEDIUM).until(
        EC.url_contains("/login")
    )

    logger.info("Пользователь успешно зарегистрирован")

    return test_credentials


@pytest.fixture
def logged_in_driver(driver, registered_user):
    """
    Фикстура: авторизует зарегистрированного пользователя.

    Returns:
        WebDriver: Браузер с авторизованной сессией
    """
    # Вход в систему
    driver.find_element(*INPUT_EMAIL_BY_LABEL).send_keys(registered_user["email"])
    driver.find_element(*INPUT_PASSWORD).send_keys(registered_user["password"])
    driver.find_element(*BUTTON_LOGIN).click()

    # Ожидание успешного входа
    WebDriverWait(driver, TIMEOUT_MEDIUM).until(
        EC.visibility_of_element_located((By.XPATH, TEXT_PERSONAL_ACCOUNT))
    )

    # Переход в личный кабинет
    driver.find_element(*LINK_PERSONAL_ACCOUNT).click()
    WebDriverWait(driver, TIMEOUT_MEDIUM).until(
        EC.url_contains(ACCOUNT_URL)
    )

    logger.info("Пользователь успешно авторизован и находится в Личном Кабинете")

    return driver