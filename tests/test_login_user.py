from pages.main_page import MainPage
from pages.login_form_page import LoginFormPage


class TestLoginUser:
    def test_login_user(self, driver):
        main_page = MainPage(driver)
        login_form_page = LoginFormPage(driver)

        main_page.open_login_form()
        login_form_page.open_registration_form()
        already_existing_email = login_form_page.create_new_account()
        main_page.logout_from_account()
        main_page.open_login_form()
        login_form_page.login_in_existing_account(already_existing_email, "123")

        assert main_page.is_user_icon_displayed()
        assert main_page.get_username_text() == "User."