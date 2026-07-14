from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

logger = logging.getLogger(__name__)

class TestAccount:
    def test_click_personal_account_when_logged(self,logged_in_driver):
        """Проверка перехода по клику на 'Личный Кабинет' при авторизованном пользователе"""
        driver = logged_in_driver
        driver.get("https://stellarburgers.education-services.ru/")

        url_before = driver.current_url
        logger.info(f"URL до клика: {url_before}")

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Личный Кабинет"))
        ).click()

        WebDriverWait(driver, 10).until(
            lambda d: d.current_url != url_before
        )

        url_after = driver.current_url
        logger.info(f"URL после клика: {url_after}")

        assert url_after != url_before, "URL не изменился после клика!"

        assert "/account" in url_after or "/profile" in url_after, f"Неверный URL: {url_after}"

        logger.info("✅ Переход в Личный Кабинет выполнен!")