from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers import generate_email, generate_name
import logging

logger = logging.getLogger(__name__)

class TestRegistrationErrors:
    def test_registration_with_short_password_error(self, driver):
        """Проверка ошибки при коротком пароле (< 6 символов)"""
        driver.get("https://stellarburgers.education-services.ru/")

        email = generate_email()
        password = '12345'
        name = generate_name()

        logger.info(f"\nСгенерированный email: {email}")
        logger.info(f"Сгенерированный пароль: {password}")
        logger.info(f"Сгенерированное имя: {name}\n")

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Войти в аккаунт']"))
        ).click()

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Зарегистрироваться"))
        ).click()

        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "name"))
        )


        driver.find_element(By.XPATH, "//label[text()='Имя']/following-sibling::input").send_keys(name)
        driver.find_element(By.XPATH, "//label[text()='Email']/following-sibling::input").send_keys(email)
        driver.find_element(By.NAME, "Пароль").send_keys(password)
        driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']").click()

        error_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//p[contains(text(), 'Некорректный пароль')]"))
        )
        assert "Некорректный пароль" in error_message.text, f"Неверный текст ошибки: {error_message.text}"
        logger.info("Ошибка при коротком пароле отображается!")
        logger.info(f"Текст ошибки: {error_message.text}")


