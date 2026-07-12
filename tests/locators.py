from selenium.webdriver.common.by import By

# Шапка сайта
HEADER_NAV = (By.CLASS_NAME, "AppHeader_header__nav__g5hnF")

# Логотип Stellar Burgers (ссылка на главную)
LOGO_LINK = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2")

# Ссылка "Конструктор" в шапке
LINK_CONSTRUCTOR = (By.LINK_TEXT, "Конструктор")

# Ссылка "Личный Кабинет" в шапке
LINK_PERSONAL_ACCOUNT = (By.LINK_TEXT, "Личный Кабинет")

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

# Активная вкладка (любая с классом tab_tab_type_current)
TAB_ACTIVE = (By.CLASS_NAME, "tab_tab_type_current__2BEPc")

# Заголовок раздела "Булки"
HEADER_BUNS_SECTION = (By.XPATH, "//h2[contains(text(), 'Булки')]")

# Заголовок раздела "Соусы"
HEADER_SAUCE_SECTION = (By.XPATH, "//h2[contains(text(), 'Соусы')]")

# Заголовок раздела "Начинки"
HEADER_FILLING_SECTION = (By.XPATH, "//h2[contains(text(), 'Начинки')]")

# Список ингредиентов
INGREDIENTS_LIST = (By.CLASS_NAME, "BurgerIngredients_ingredients__list__2A-mT")

# Корзина бургера
BASKET = (By.CLASS_NAME, "BurgerConstructor_basket__29Cd7")

# Контейнер формы входа
LOGIN_CONTAINER = (By.CLASS_NAME, "Auth_login__3hAey")

# Заголовок "Вход"
HEADER_LOGIN = (By.XPATH, "//h2[contains(text(), 'Вход')]")

# Форма входа
FORM_LOGIN = (By.CLASS_NAME, "Auth_form__3qKeq")

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

# Заголовок "Регистрация"
HEADER_REGISTER = (By.XPATH, "//h2[contains(text(), 'Регистрация')]")

# Форма регистрации
FORM_REGISTER = (By.CLASS_NAME, "Auth_form__3qKeq")

# Поле ввода Имя
INPUT_NAME = (By.NAME, "name")

# Поле ввода Имя (по label)
INPUT_NAME_BY_LABEL = (By.XPATH, "//label[contains(text(), 'Имя')]/following-sibling::input")

# Кнопка "Зарегистрироваться"
BUTTON_REGISTER = (By.XPATH, "//button[text()='Зарегистрироваться']")

# Сообщение об ошибке (некорректный пароль)
ERROR_MESSAGE = (By.XPATH, "//p[contains(text(), 'Некорректный пароль')]")


# Контейнер личного кабинета
ACCOUNT_CONTAINER = (By.CLASS_NAME, "Account_account__vgk_w")

# Заголовок "Личный кабинет"
HEADER_ACCOUNT = (By.XPATH, "//h2[contains(text(), 'Личный кабинет')]")

# Кнопка "Выход"
BUTTON_LOGOUT = (By.XPATH, "//button[contains(text(), 'Выход')]")

# Текст с информацией о разделе
ACCOUNT_INFO_TEXT = (By.CLASS_NAME, "Account_text__fZAIn")

# Активная ссылка "Личный Кабинет" (с классом link_active)
LINK_ACCOUNT_ACTIVE = (By.CLASS_NAME, "AppHeader_header__link_active__1IkJo")


# URL главной страницы
URL_MAIN = "https://stellarburgers.education-services.ru/"

# URL страницы входа
URL_LOGIN = "/login"

# URL личного кабинета
URL_ACCOUNT = "/account"

# URL восстановления пароля
URL_RECOVER_PASSWORD = "/forgot-password"