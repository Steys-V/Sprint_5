from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

logger = logging.getLogger(__name__)

class TestLogout:
    """Тесты выхода из аккаунта"""
    def test_logout_button(self,logged_in_driver):
        """Проверка выхода из аккаунта по кнопке 'Выйти' в Личном Кабинете"""
        driver = logged_in_driver

        driver.get("https://stellarburgers.education-services.ru/account")

        WebDriverWait(driver, 10).until(
            EC.url_contains("/account")
        )
        assert "/account" in driver.current_url
        logger.info("Находимся в Личном Кабинете")

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Выход')]"))
        ).click()

        logger.info("Кнопка 'Выход' нажата")

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "Auth_login__3hAey"))
        )

        WebDriverWait(driver, 10).until(
            EC.url_contains("/login")
        )
        assert "/login" in driver.current_url

        header = driver.find_element(By.XPATH, "//h2[contains(text(), 'Вход')]")
        assert header.is_displayed()

        logger.info("Выход из аккаунта выполнен! Открыта страница входа.")



