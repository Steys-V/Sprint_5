from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers import generate_email, generate_password, generate_name

def test_registration(driver: webdriver.Chrome):
    """Проверка успешной регистрации"""
    driver.get("https://stellarburgers.education-services.ru/")

    email = generate_email()
    password = generate_password()
    name = generate_name()

    print(f"\nСгенерированный email: {email}")
    print(f"Сгенерированный пароль: {password}")
    print(f"Сгенерированное имя: {name}\n")

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

    WebDriverWait(driver, 10).until(
        EC.url_contains("/login")
    )
    print(f"✅ Регистрация успешна для пользователя: {email}")


