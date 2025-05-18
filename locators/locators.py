from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Вход и регистрация')]")
    CREATE_ADVERTISEMENT_BUTTON = (By.XPATH, "//button[contains(text(), 'Разместить объявление')]")
    USER_ICON = (By.CSS_SELECTOR, 'svg.svgSmall')
    USER_NAME = (By.CSS_SELECTOR, "h3.profileText.name")
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выйти')]")

class LoginFormLocators:
    NO_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(), 'Нет аккаунта')]")
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    SUBMIT_PASSWORD_INPUT = (By.NAME, "submitPassword")
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(), 'Создать аккаунт')]")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".input_span__yWPqB")

class ProfilePageLocators:
    CREATED_ADVERTISEMENT = (By.CSS_SELECTOR, "div.card")

class CreationNewAdvertisementLocators:
    TITLE_INPUT = (By.NAME, "name")
    DESCRIPTION_INPUT = (By.XPATH, "//textarea[@name='description']")
    PRICE_INPUT = (By.NAME, "price")
    SELECT_CATEGORY_DROPDOWN_BUTTON = (By.XPATH, "//input[@name='category']/following-sibling::button")
    GARDEN_CHOICE = (By.XPATH, "//span[@class='undefined dropDownMenu_textColor__Nyo8k' and text()='Садоводство']")
    SELECT_CITY_DROPDOWN_BUTTON = (By.XPATH,"//input[@name='city']/following-sibling::button")
    EKB_CITY_CHOICE = (By.XPATH, "//span[@class='undefined dropDownMenu_textColor__Nyo8k' and text()='Екатеринбург']")
    PUBLISH_AD_BUTTON = (By.XPATH, "//button[contains(text(), 'Опубликовать')]")


class PopupFormLocators:
    POPUP_TITLE = (By.CSS_SELECTOR, ".popUp_titleRow__M7tGg")
