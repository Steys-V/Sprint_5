from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helpers import generate_email, generate_password, generate_name

def test_registration(driver: webdriver.Chrome):
    """Проверка ошибки при коротком пароле (< 6 символов)"""
    driver.get("https://stellarburgers.education-services.ru/")

    email = generate_email()
    password = '12345'
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

    error_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//p[contains(text(), 'Некорректный пароль')]"))
    )
    assert error_message.is_displayed(), "Сообщение об ошибке не появилось!"
    assert "Некорректный пароль" in error_message.text, f"Неверный текст ошибки: {error_message.text}"
    print("✅ Ошибка при коротком пароле отображается!")
    print("Текст ошибки:", error_message.text)


