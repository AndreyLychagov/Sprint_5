from pages.base_page import BasePage
from locators.locators import MainPageLocators, PopupFormLocators


class MainPage(BasePage):
    def open_login_form(self):
        self.click(MainPageLocators.LOGIN_BUTTON)

    def click_create_advertisement(self):
        self.click(MainPageLocators.CREATE_ADVERTISEMENT_BUTTON)

    def is_user_icon_displayed(self):
        return self.is_element_visible(MainPageLocators.USER_ICON)

    def get_username_text(self):
        return self.get_element_text(MainPageLocators.USER_NAME)

    def logout_from_account(self):
        self.click(MainPageLocators.LOGOUT_BUTTON)

    def is_login_button_displayed(self):
        return self.is_element_visible(MainPageLocators.LOGIN_BUTTON)

    def popup_title(self):
        return self.driver.find_element(*PopupFormLocators.POPUP_TITLE).text

    def open_user_profile(self):
        self.click(MainPageLocators.USER_ICON)