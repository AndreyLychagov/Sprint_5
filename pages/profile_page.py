from pages.base_page import BasePage
from locators.locators import ProfilePageLocators


class ProfilePage(BasePage):
    def find_created_advertisement(self):
        return self.is_element_visible(ProfilePageLocators.CREATED_ADVERTISEMENT)
