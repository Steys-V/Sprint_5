from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

logger = logging.getLogger(__name__)

class TestLogin:

    def test_login_via_registration_form(self,driver: webdriver.Chrome):
        """Проверка входа через ссылку 'Войти' в форме регистрации"""
        driver.get("https://stellarburgers.education-services.ru/")

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Войти в аккаунт']"))
        ).click()

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Зарегистрироваться"))
        ).click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(), 'Регистрация')]"))
        )

        driver.find_element(By.LINK_TEXT, "Войти").click()

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

        logger.info("Вход через ссылку 'Войти' в форме регистрации выполнен успешно!")
        logger.info(f"Текущий URL: {driver.current_url}")
