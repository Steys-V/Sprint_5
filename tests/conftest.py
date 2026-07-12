import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers import generate_email, generate_password
import time

@pytest.fixture
def driver():
    """Фикстура: создаёт и закрывает браузер"""
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    browser.quit()


@pytest.fixture
def logged_in_driver(driver):
    """Фикстура: авторизованный драйвер с уникальным пользователем"""
    driver.get("https://stellarburgers.education-services.ru/")

    email = generate_email()
    password = generate_password()

    print(f"\n📧 Тестовый email: {email}")
    print(f"🔑 Тестовый пароль: {password}\n")

    driver.find_element(By.XPATH, '//button[text()="Войти в аккаунт"]').click()
    driver.find_element(By.LINK_TEXT, "Зарегистрироваться").click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, "name"))
    )

    driver.find_element(By.NAME, "name").send_keys("Тест")
    driver.find_element(By.XPATH, "//label[contains(text(), 'Email')]/following-sibling::input").send_keys(email)
    driver.find_element(By.NAME, "Пароль").send_keys(password)
    driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']").click()

    WebDriverWait(driver, 10).until(EC.url_contains("/login"))

    driver.find_element(By.XPATH, "//label[contains(text(), 'Email')]/following-sibling::input").send_keys(email)
    driver.find_element(By.NAME, "Пароль").send_keys(password)
    driver.find_element(By.XPATH, "//button[text()='Войти']").click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//p[contains(text(), 'Личный Кабинет')]"))
    )

    print("✅ Пользователь успешно авторизован!\n")
    time.sleep(1)  # Даём сайту время установить сессию

    account_link = driver.find_element(By.LINK_TEXT, "Личный Кабинет")
    driver.execute_script("arguments[0].click();", account_link)

    WebDriverWait(driver, 10).until(EC.url_contains("/account"))
    print("✅ Перешли в Личный Кабинет\n")

    return driver