from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

logger = logging.getLogger(__name__)


class TestMainPageLogin:
    """Тесты входа с главной страницы"""
    def test_login_via_main_button(self,driver: webdriver.Chrome):
        """Проверка входа через кнопку 'Войти в аккаунт' с заполнением полей"""
        driver.get("https://stellarburgers.education-services.ru/")

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[text()="Войти в аккаунт"]'))
        ).click()


        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "Auth_form__3qKeq"))
        )

        driver.find_element(By.XPATH, "//label[contains(text(), 'Email')]/following-sibling::input").send_keys("vorobevaanastasia.50123@gmail.ru")
        driver.find_element(By.NAME, "Пароль").send_keys("nasty1304")
        driver.find_element(By.XPATH, "//button[text()='Войти']").click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//p[contains(text(), 'Личный Кабинет')]"))
        )
        assert driver.find_element(By.XPATH, "//p[contains(text(), 'Личный Кабинет')]").is_displayed()

        logger.info("Вход через кнопку 'Войти в аккаунт' выполнен успешно!")
        logger.info(f'Текущий URL : {driver.current_url}')

