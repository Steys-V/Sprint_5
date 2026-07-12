from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_buns_section_click(driver):
    """Проверка клика на вкладку 'Булки' в Конструкторе"""
    driver.get("https://stellarburgers.education-services.ru/")

    WebDriverWait(driver, 10).until(
        EC.url_to_be("https://stellarburgers.education-services.ru/")
    )
    print("✅ Конструктор открыт")

    buns_tab = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Булки')]"))
    )
    driver.execute_script("arguments[0].click();", buns_tab)
    print("✅ Кликнули на вкладку 'Булки'")

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]//span[contains(text(), 'Булки')]"))
    )

    buns_header = driver.find_element(By.XPATH, "//h2[contains(text(), 'Булки')]")
    assert buns_header.is_displayed(), "Раздел 'Булки' не отображается!"

    print("✅ Вкладка 'Булки' активна, раздел отображается!")


def test_sauces_section(driver):
    """Проверка клика на вкладку 'Соусы' в Конструкторе"""
    driver.get("https://stellarburgers.education-services.ru/")

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Соусы')]"))
    )

    sauces_tab = driver.find_element(By.XPATH, "//span[contains(text(), 'Соусы')]")
    driver.execute_script("arguments[0].click();", sauces_tab)
    print("✅ Кликнули на вкладку 'Соусы'")

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]//span[contains(text(), 'Соусы')]"))
    )

    sauces_header = driver.find_element(By.XPATH, "//h2[contains(text(), 'Соусы')]")
    assert sauces_header.is_displayed(), "Раздел 'Соусы' не отображается!"

    print("✅ Вкладка 'Соусы' активна, раздел отображается!")


def test_filling_section(driver):
    """Проверка клика на вкладку 'Начинки' в Конструкторе"""
    driver.get("https://stellarburgers.education-services.ru/")

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'Начинки')]"))
    )

    filling_tab = driver.find_element(By.XPATH, "//span[contains(text(), 'Начинки')]")
    driver.execute_script("arguments[0].click();", filling_tab)
    print("✅ Кликнули на вкладку 'Начинки'")

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]//span[contains(text(), 'Начинки')]"))
    )

    filling_header = driver.find_element(By.XPATH, "//h2[contains(text(), 'Начинки')]")
    assert filling_header.is_displayed(), "Раздел 'Начинки' не отображается!"

    print("✅ Вкладка 'Начинки' активна, раздел отображается!")


def test_all_sections_navigation(driver):
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
    print("✅ Вкладка 'Булки' активна")

    sauces_tab = driver.find_element(By.XPATH, "//span[contains(text(), 'Соусы')]")
    driver.execute_script("arguments[0].click();", sauces_tab)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]//span[contains(text(), 'Соусы')]"))
    )
    print("✅ Вкладка 'Соусы' активна")


    filling_tab = driver.find_element(By.XPATH, "//span[contains(text(), 'Начинки')]")
    driver.execute_script("arguments[0].click();", filling_tab)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]//span[contains(text(), 'Начинки')]"))
    )
    print("✅ Вкладка 'Начинки' активна")