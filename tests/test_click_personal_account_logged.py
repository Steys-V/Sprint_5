from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_click_personal_account_when_logged(logged_in_driver):
    """Проверка перехода по клику на 'Личный Кабинет' при авторизованном пользователе"""
    driver = logged_in_driver
    driver.get("https://stellarburgers.education-services.ru/")

    url_before = driver.current_url
    print(f"🔗 URL до клика: {url_before}")

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Личный Кабинет"))
    ).click()

    WebDriverWait(driver, 10).until(
        lambda d: d.current_url != url_before
    )

    # Показываем новый URL
    url_after = driver.current_url
    print(f"🔗 URL после клика: {url_after}")

    # ✅ ПРОВЕРКА: URL изменился
    assert url_after != url_before, "URL не изменился после клика!"

    # ✅ ПРОВЕРКА: URL содержит /account или /profile
    assert "/account" in url_after or "/profile" in url_after, f"Неверный URL: {url_after}"

    print("✅ Переход в Личный Кабинет выполнен!")