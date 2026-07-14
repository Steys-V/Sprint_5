import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LOGO_LINK, LINK_CONSTRUCTOR
from config import BASE_URL

logger = logging.getLogger(__name__)


class TestConstructorNavigation:
    """Тесты перехода из Личного Кабинета в Конструктор"""

    def test_from_account_to_constructor_by_link(self, logged_in_driver):
        """Проверка перехода из Личного Кабинета в Конструктор по клику на 'Конструктор'"""
        driver = logged_in_driver

        driver.get(f"{BASE_URL}account")
        WebDriverWait(driver, 10).until(EC.url_contains("/account"))

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LINK_CONSTRUCTOR)
        ).click()

        WebDriverWait(driver, 10).until(EC.url_to_be(BASE_URL))
        assert driver.current_url == BASE_URL

        logger.info("Переход в Конструктор по ссылке выполнен успешно")

    def test_from_account_to_constructor_by_logo(self, logged_in_driver):
        """Проверка перехода из Личного Кабинета в Конструктор по клику на логотип"""
        driver = logged_in_driver

        driver.get(f"{BASE_URL}account")
        WebDriverWait(driver, 10).until(EC.url_contains("/account"))

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LOGO_LINK)
        ).click()

        WebDriverWait(driver, 10).until(EC.url_to_be(BASE_URL))
        assert driver.current_url == BASE_URL

        logger.info("Переход в Конструктор по логотипу выполнен успешно")

    def test_logo_is_visible_on_constructor(self, logged_in_driver):
        """Проверка, что логотип отображается на странице Конструктора"""
        driver = logged_in_driver

        driver.get(f"{BASE_URL}account")
        WebDriverWait(driver, 10).until(EC.url_contains("/account"))

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LINK_CONSTRUCTOR)
        ).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(BASE_URL))

        logo = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LOGO_LINK)
        )
        assert logo.is_displayed()

        logger.info("Логотип отображается на странице Конструктора")

    def test_logo_has_correct_href(self, logged_in_driver):
        """Проверка, что логотип ведёт на главную страницу"""
        driver = logged_in_driver

        driver.get(f"{BASE_URL}account")
        WebDriverWait(driver, 10).until(EC.url_contains("/account"))

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LINK_CONSTRUCTOR)
        ).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(BASE_URL))

        logo_link = driver.find_element(*LOGO_LINK)
        assert logo_link.get_attribute("href") == BASE_URL

        logger.info("Логотип имеет корректную ссылку на главную страницу")