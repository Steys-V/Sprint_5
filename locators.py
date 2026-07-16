from selenium.webdriver.common.by import By


# ==========================================
# ШАПКА САЙТА
# ==========================================

# Навигационное меню (по тегу nav)
HEADER_NAV = (By.TAG_NAME, "nav")

# Логотип Stellar Burgers (ссылка с href="/")
LOGO_LINK = (By.CSS_SELECTOR, "a[href='/']")

# Контейнер логотипа (для проверки видимости)
LOGO_CONTAINER = (By.CSS_SELECTOR, "[class*='logo'] svg")

# Ссылка "Конструктор" в шапке
LINK_CONSTRUCTOR = (By.LINK_TEXT, "Конструктор")

# Ссылка "Личный Кабинет" в шапке
LINK_PERSONAL_ACCOUNT = (By.LINK_TEXT, "Личный Кабинет")


# ==========================================
# ГЛАВНАЯ СТРАНИЦА (КОНСТРУКТОР)
# ==========================================

# Кнопка "Войти в аккаунт" на главной
BUTTON_LOGIN_MAIN = (By.XPATH, '//button[text()="Войти в аккаунт"]')

# Заголовок "Соберите бургер"
HEADER_CONSTRUCTOR = (By.XPATH, "//h1[contains(text(), 'Соберите бургер')]")

# Вкладка "Булки"
TAB_BUNS = (By.XPATH, "//span[contains(text(), 'Булки')]")

# Вкладка "Соусы"
TAB_SAUCE = (By.XPATH, "//span[contains(text(), 'Соусы')]")

# Вкладка "Начинки"
TAB_FILLING = (By.XPATH, "//span[contains(text(), 'Начинки')]")

# Активная вкладка (по атрибуту или тексту)
TAB_ACTIVE = (By.CSS_SELECTOR, "[class*='tab_tab_type_current']")

# Активная вкладка "Булки"
TAB_ACTIVE_BUNS = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]/span[contains(text(), 'Булки')]")

# Активная вкладка "Соусы"
TAB_ACTIVE_SAUCE = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]/span[contains(text(), 'Соусы')]")

# Активная вкладка "Начинки"
TAB_ACTIVE_FILLING = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]/span[contains(text(), 'Начинки')]")

# Заголовок раздела "Булки"
HEADER_BUNS_SECTION = (By.XPATH, "//h2[contains(text(), 'Булки')]")

# Заголовок раздела "Соусы"
HEADER_SAUCE_SECTION = (By.XPATH, "//h2[contains(text(), 'Соусы')]")

# Заголовок раздела "Начинки"
HEADER_FILLING_SECTION = (By.XPATH, "//h2[contains(text(), 'Начинки')]")

# Список ингредиентов (по data-testid или структуре)
INGREDIENTS_LIST = (By.CSS_SELECTOR, "[class*='ingredients'][class*='list']")

# Корзина бургера
BASKET = (By.CSS_SELECTOR, "[class*='basket']")


# ==========================================
# СТРАНИЦА ВХОДА (/login)
# ==========================================

# Контейнер формы входа (по структуре)
LOGIN_CONTAINER = (By.CSS_SELECTOR, "[class*='Auth'][class*='login']")

# Заголовок "Вход"
HEADER_LOGIN = (By.XPATH, "//h2[contains(text(), 'Вход')]")

# Форма входа
FORM_LOGIN = (By.CSS_SELECTOR, "form[class*='Auth']")

# Поле ввода Email
INPUT_EMAIL = (By.NAME, "email")

# Поле ввода Email (по label)
INPUT_EMAIL_BY_LABEL = (By.XPATH, "//label[contains(text(), 'Email')]/following-sibling::input")

# Поле ввода Пароль
INPUT_PASSWORD = (By.NAME, "Пароль")

# Кнопка "Войти"
BUTTON_LOGIN = (By.XPATH, "//button[text()='Войти']")

# Ссылка "Зарегистрироваться"
LINK_REGISTER = (By.LINK_TEXT, "Зарегистрироваться")

# Ссылка "Восстановить пароль"
LINK_RECOVER_PASSWORD = (By.LINK_TEXT, "Восстановить пароль")

# Ссылка "Войти" (в форме регистрации/восстановления)
LINK_LOGIN = (By.LINK_TEXT, "Войти")

# Текст "Уже зарегистрированы?"
TEXT_ALREADY_REGISTERED = (By.XPATH, "//p[contains(text(), 'Уже зарегистрированы?')]")


# ==========================================
# СТРАНИЦА РЕГИСТРАЦИИ
# ==========================================

# Заголовок "Регистрация"
HEADER_REGISTER = (By.XPATH, "//h2[contains(text(), 'Регистрация')]")

# Форма регистрации
FORM_REGISTER = (By.CSS_SELECTOR, "form[class*='Auth']")

# Поле ввода Имя
INPUT_NAME = (By.NAME, "name")

# Поле ввода Имя (по label)
INPUT_NAME_BY_LABEL = (By.XPATH, "//label[contains(text(), 'Имя')]/following-sibling::input")

# Кнопка "Зарегистрироваться"
BUTTON_REGISTER = (By.XPATH, "//button[text()='Зарегистрироваться']")

# Сообщение об ошибке (некорректный пароль)
ERROR_MESSAGE = (By.XPATH, "//p[contains(text(), 'Некорректный пароль')]")


# ==========================================
# ЛИЧНЫЙ КАБИНЕТ
# ==========================================

# Контейнер личного кабинета
ACCOUNT_CONTAINER = (By.CSS_SELECTOR, "[class*='Account'][class*='account']")

# Заголовок "Личный кабинет"
HEADER_ACCOUNT = (By.XPATH, "//h2[contains(text(), 'Личный кабинет')]")

# Текст "Личный Кабинет" (для проверки успешного входа)
TEXT_PERSONAL_ACCOUNT = "//p[contains(text(), 'Личный Кабинет')]"

# Кнопка "Выход"
BUTTON_LOGOUT = (By.XPATH, "//button[contains(text(), 'Выход')]")

# Текст с информацией о разделе
ACCOUNT_INFO_TEXT = (By.CSS_SELECTOR, "[class*='Account_text']")

# Активная ссылка "Личный Кабинет" (по data-testid или aria-current)
LINK_ACCOUNT_ACTIVE = (By.CSS_SELECTOR, "[aria-current='page']")