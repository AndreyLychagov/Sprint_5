from pages.main_page import MainPage
from pages.login_form_page import LoginFormPage


class TestLogoutUser:
    def test_logout_user(self, driver):
        main_page = MainPage(driver)
        login_form_page = LoginFormPage(driver)

        main_page.open_login_form()
        login_form_page.open_registration_form()
        login_form_page.create_new_account()
        main_page.logout_from_account()

        assert main_page.is_login_button_displayed()
        assert not main_page.is_user_icon_displayed()
