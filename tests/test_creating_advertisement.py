from pages.profile_page import ProfilePage
from pages.main_page import MainPage
from pages.login_form_page import LoginFormPage

class TestCreatingAdvertisement:
    def test_ad_creation_by_unauthorized_user(self, driver):
        main_page = MainPage(driver)
        main_page.click_create_advertisement()

        main_page.popup_title()
        assert main_page.popup_title() == "Чтобы разместить объявление, авторизуйтесь"

    def test_creation_advertisement_by_authorized_user(self, driver):
        main_page = MainPage(driver)
        login_form_page = LoginFormPage(driver)
        profile_page = ProfilePage(driver)

        main_page.open_login_form()
        login_form_page.open_registration_form()
        login_form_page.create_new_account()
        assert main_page.is_user_icon_displayed()
        main_page.click_create_advertisement()
        profile_page.fill_title('Тестовое объявление')
        profile_page.fill_description('Тестовое описание')
        profile_page.fill_price('123')
        profile_page.select_category()
        profile_page.select_city()
        profile_page.publish_advertisement()
        profile_page.open_user_profile()
        assert profile_page.find_created_advertisement()
