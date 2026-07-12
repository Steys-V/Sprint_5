from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_from_account_to_constructor_by_link(logged_in_driver):
    """Проверка перехода из Личного Кабинета в Конструктор по клику на 'Конструктор'"""
    driver = logged_in_driver

    driver.get("https://stellarburgers.education-services.ru/account")
    WebDriverWait(driver, 10).until(EC.url_contains("/account"))
    assert "/account" in driver.current_url
    print("✅ Находимся в Личном Кабинете")

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Конструктор"))
    ).click()

    WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.education-services.ru/"))
    assert driver.current_url == "https://stellarburgers.education-services.ru/"

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "AppHeader_header__logo__2D0X2"))
    )
    logo_link = driver.find_element(By.CSS_SELECTOR, ".AppHeader_header__logo__2D0X2 a")
    assert logo_link.get_attribute("href") == "https://stellarburgers.education-services.ru/"

    print("✅ Переход в Конструктор выполнен! Логотип Stellar Burgers отображается.")
    

