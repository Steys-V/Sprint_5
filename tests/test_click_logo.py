from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
from locators import LOGO_LINK
from config import BASE_URL

logger = logging.getLogger(__name__)

class TestConstructorNavigation:
    """Тесты перехода из Личного Кабинета в Конструктор"""
    def test_from_account_to_constructor_by_logo(self,logged_in_driver):
        """Проверка перехода из Личного Кабинета в Конструктор по клику на логотип"""
        driver = logged_in_driver

        driver.get(f"{BASE_URL}account")
        WebDriverWait(driver, 10).until(EC.url_contains("/account"))
        assert "/account" in driver.current_url
        logger.info("Находимся в Личном Кабинете")

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LOGO_LINK)
        ).click()

        WebDriverWait(driver, 10).until(
            EC.url_to_be(BASE_URL)
        )
        assert driver.current_url == BASE_URL

        logo = driver.find_element(*LOGO_LINK)
        assert logo.is_displayed()

        logger.info("Переход в Конструктор выполнен! Логотип Stellar Burgers отображается.")