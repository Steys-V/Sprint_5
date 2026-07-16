import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import (
    BUTTON_LOGIN_MAIN,
    LINK_PERSONAL_ACCOUNT,
    LINK_REGISTER,
    LINK_RECOVER_PASSWORD,
    LINK_LOGIN,
    INPUT_EMAIL_BY_LABEL,
    INPUT_PASSWORD,
    BUTTON_LOGIN,
    HEADER_LOGIN,
    TEXT_PERSONAL_ACCOUNT
)
from config import BASE_URL

logger = logging.getLogger(__name__)


class TestLogin:
    """Тесты входа в аккаунт через различные точки входа"""

    def test_login_via_main_button(self, driver):
        """Проверка входа через кнопку 'Войти в аккаунт' на главной странице"""
        driver.get(BASE_URL)

        driver.find_element(*BUTTON_LOGIN_MAIN).click()

        header = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(HEADER_LOGIN)
        )
        assert header.is_displayed()

        logger.info("Вход через кнопку на главной выполнен успешно")

    def test_login_via_personal_account_button(self, driver):
        """Проверка входа через кнопку 'Личный Кабинет'"""
        driver.get(BASE_URL)

        driver.find_element(*LINK_PERSONAL_ACCOUNT).click()

        header = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(HEADER_LOGIN)
        )
        assert header.is_displayed()

        logger.info("Вход через кнопку 'Личный Кабинет' выполнен успешно")

    def test_login_via_registration_form(self, driver):
        """Проверка входа через ссылку 'Войти' в форме регистрации"""
        driver.get(BASE_URL)

        driver.find_element(*BUTTON_LOGIN_MAIN).click()
        driver.find_element(*LINK_REGISTER).click()

        driver.find_element(*LINK_LOGIN).click()

        header = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(HEADER_LOGIN)
        )
        assert header.is_displayed()

        logger.info("Вход через форму регистрации выполнен успешно")

    def test_login_via_password_recovery_form(self, driver):
        """Проверка входа через ссылку 'Войти' на странице восстановления пароля"""
        driver.get(BASE_URL)

        driver.find_element(*BUTTON_LOGIN_MAIN).click()
        driver.find_element(*LINK_RECOVER_PASSWORD).click()

        driver.find_element(*LINK_LOGIN).click()

        header = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(HEADER_LOGIN)
        )
        assert header.is_displayed()

        logger.info("Вход через форму восстановления пароля выполнен успешно")