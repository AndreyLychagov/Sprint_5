import uuid
from pages.base_page import BasePage
from locators.locators import LoginFormLocators


class LoginFormPage(BasePage):
    def open_registration_form(self):
        self.click(LoginFormLocators.NO_ACCOUNT_BUTTON)

    def create_new_account(self, email=None, password="123"):
        if email is None:
            email = f"random_{uuid.uuid4().hex[:4]}@mailbox.com"

        self.send_keys(LoginFormLocators.EMAIL_INPUT, email)
        self.send_keys(LoginFormLocators.PASSWORD_INPUT, password)
        self.send_keys(LoginFormLocators.SUBMIT_PASSWORD_INPUT, password)
        self.click(LoginFormLocators.CREATE_ACCOUNT_BUTTON)

        return email

    def wrong_field_mask(self, email):
        self.send_keys(LoginFormLocators.EMAIL_INPUT, email)
        self.click(LoginFormLocators.CREATE_ACCOUNT_BUTTON)

    def is_error_message_displayed(self):
        return self.is_element_visible(LoginFormLocators.ERROR_MESSAGE)

    def login_in_existing_account(self, email, password):
        self.send_keys(LoginFormLocators.EMAIL_INPUT, email)
        self.send_keys(LoginFormLocators.PASSWORD_INPUT, password)
        self.click(LoginFormLocators.LOGIN_BUTTON)
