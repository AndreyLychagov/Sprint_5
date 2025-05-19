from pages.main_page import MainPage
from pages.login_form_page import LoginFormPage


class TestUserRegistration:
    def test_user_registration(self, driver):
        main_page = MainPage(driver)
        login_form_page = LoginFormPage(driver)

        main_page.open_login_form()
        login_form_page.open_registration_form()
        login_form_page.create_new_account()

        assert main_page.is_user_icon_displayed()
        assert main_page.get_username_text() == "User."

    def test_wrong_field_mask_registration(self, driver):
        main_page = MainPage(driver)
        login_form_page = LoginFormPage(driver)

        main_page.open_login_form()
        login_form_page.open_registration_form()
        login_form_page.wrong_field_mask("wrong_email")

        assert login_form_page.is_error_message_displayed()

    def test_registration_existing_user(self, driver):
        main_page = MainPage(driver)
        login_form_page = LoginFormPage(driver)

        main_page.open_login_form()
        login_form_page.open_registration_form()
        already_existing_email = login_form_page.create_new_account()
        main_page.logout_from_account()
        main_page.open_login_form()
        login_form_page.open_registration_form()
        login_form_page.create_new_account(email=already_existing_email, password="123")

        assert login_form_page.is_error_message_displayed()