from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_from_account_to_constructor_by_logo(logged_in_driver):
    """Проверка перехода из Личного Кабинета в Конструктор по клику на логотип"""
    driver = logged_in_driver

    driver.get("https://stellarburgers.education-services.ru/account")
    WebDriverWait(driver, 10).until(EC.url_contains("/account"))
    assert "/account" in driver.current_url
    print("✅ Находимся в Личном Кабинете")

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".AppHeader_header__logo__2D0X2 a"))
    ).click()

    WebDriverWait(driver, 10).until(
        EC.url_to_be("https://stellarburgers.education-services.ru/")
    )
    assert driver.current_url == "https://stellarburgers.education-services.ru/"

    logo = driver.find_element(By.CLASS_NAME, "AppHeader_header__logo__2D0X2")
    assert logo.is_displayed()

    print("✅ Переход в Конструктор выполнен! Логотип Stellar Burgers отображается.")