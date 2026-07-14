from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import logging

logger = logging.getLogger(__name__)

class TestConstructorSections:
    """Тесты переключения разделов конструктора"""
    def test_buns_section_click(self,driver):
        """Проверка клика на вкладку 'Булки' в Конструкторе"""
        driver.get("https://stellarburgers.education-services.ru/")

        WebDriverWait(driver, 10).until(
            EC.url_to_be("https://stellarburgers.education-services.ru/")
        )
        logger.info("Конструктор открыт")

        buns_tab = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Булки')]"))
        )
        driver.execute_script("arguments[0].click();", buns_tab)
        logger.info("Кликнули на вкладку 'Булки'")

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]//span[contains(text(), 'Булки')]"))
        )

        buns_header = driver.find_element(By.XPATH, "//h2[contains(text(), 'Булки')]")
        assert buns_header.is_displayed(), "Раздел 'Булки' не отображается!"

        logger.info("Вкладка 'Булки' активна раздел отображается!")


    def test_sauces_section(self,driver):
        """Проверка клика на вкладку 'Соусы' в Конструкторе"""
        driver.get("https://stellarburgers.education-services.ru/")

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Соусы')]"))
        )

        sauces_tab = driver.find_element(By.XPATH, "//span[contains(text(), 'Соусы')]")
        driver.execute_script("arguments[0].click();", sauces_tab)
        logger.info("Кликнули на вкладку 'Соусы'")

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]//span[contains(text(), 'Соусы')]"))
        )

        sauces_header = driver.find_element(By.XPATH, "//h2[contains(text(), 'Соусы')]")
        assert sauces_header.is_displayed(), "Раздел 'Соусы' не отображается!"

        logger.info(f"Вкладка 'Соусы' активна раздел отображается!")


    def test_filling_section(self,driver):
        """Проверка клика на вкладку 'Начинки' в Конструкторе"""
        driver.get("https://stellarburgers.education-services.ru/")

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Начинки')]"))
        )

        filling_tab = driver.find_element(By.XPATH, "//span[contains(text(), 'Начинки')]")
        driver.execute_script("arguments[0].click();", filling_tab)
        logger.info("Кликнули на вкладку 'Начинки'")

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]//span[contains(text(), 'Начинки')]"))
        )

        filling_header = driver.find_element(By.XPATH, "//h2[contains(text(), 'Начинки')]")
        assert filling_header.is_displayed(), "Раздел 'Начинки' не отображается!"

        logger.info("Вкладка 'Начинки' активна раздел отображается!")


    def test_all_sections_navigation(self,driver):
        """Проверка переключения между всеми разделами: Булки, Соусы, Начинки"""
        driver.get("https://stellarburgers.education-services.ru/")

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Булки')]"))
        )

        buns_tab = driver.find_element(By.XPATH, "//span[contains(text(), 'Булки')]")
        driver.execute_script("arguments[0].click();", buns_tab)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]//span[contains(text(), 'Булки')]"))
        )
        logger.info("Вкладка 'Булки' активна")

        sauces_tab = driver.find_element(By.XPATH, "//span[contains(text(), 'Соусы')]")
        driver.execute_script("arguments[0].click();", sauces_tab)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]//span[contains(text(), 'Соусы')]"))
        )
        logger.info("Вкладка 'Соусы' активна")


        filling_tab = driver.find_element(By.XPATH, "//span[contains(text(), 'Начинки')]")
        driver.execute_script("arguments[0].click();", filling_tab)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]//span[contains(text(), 'Начинки')]"))
        )
        logger.info("Вкладка 'Начинки' активна")