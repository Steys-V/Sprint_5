import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import (
    TAB_BUNS,
    TAB_SAUCE,
    TAB_FILLING,
    TAB_ACTIVE_BUNS,
    TAB_ACTIVE_SAUCE,
    TAB_ACTIVE_FILLING,
    HEADER_BUNS_SECTION,
    HEADER_SAUCE_SECTION,
    HEADER_FILLING_SECTION
)

logger = logging.getLogger(__name__)


class TestConstructorSections:
    """Тесты переключения разделов конструктора"""

    def test_buns_section_click(self, driver):
        """Проверка клика на вкладку 'Булки'"""
        driver.get("https://stellarburgers.education-services.ru/")

        buns_tab = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(TAB_BUNS)
        )
        driver.execute_script("arguments[0].click();", buns_tab)

        active_buns_tab = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(TAB_ACTIVE_BUNS)
        )

        assert active_buns_tab.is_displayed(), "Вкладка 'Булки' не стала активной"
        logger.info("Вкладка 'Булки' активна, раздел отображается")

    def test_sauces_section(self, driver):
        """Проверка клика на вкладку 'Соусы'"""
        driver.get("https://stellarburgers.education-services.ru/")

        sauce_tab = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(TAB_SAUCE)
        )
        driver.execute_script("arguments[0].click();", sauce_tab)

        active_sauce_tab = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(TAB_ACTIVE_SAUCE)
        )

        assert active_sauce_tab.is_displayed(), "Вкладка 'Соусы' не стала активной"
        logger.info("Вкладка 'Соусы' активна, раздел отображается")

    def test_filling_section(self, driver):
        """Проверка клика на вкладку 'Начинки'"""
        driver.get("https://stellarburgers.education-services.ru/")

        filling_tab = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(TAB_FILLING)
        )
        driver.execute_script("arguments[0].click();", filling_tab)

        active_filling_tab = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(TAB_ACTIVE_FILLING)
        )

        assert active_filling_tab.is_displayed(), "Вкладка 'Начинки' не стала активной"
        logger.info("Вкладка 'Начинки' активна, раздел отображается")