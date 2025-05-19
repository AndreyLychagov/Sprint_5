from pages.base_page import BasePage
from locators.locators import CreationNewAdvertisementLocators


class CreateAdPage(BasePage):

    def fill_title(self, title):
        self.send_keys(CreationNewAdvertisementLocators.TITLE_INPUT, title)

    def fill_description(self, description):
        self.send_keys(CreationNewAdvertisementLocators.DESCRIPTION_INPUT, description)

    def fill_price(self, price):
        self.send_keys(CreationNewAdvertisementLocators.PRICE_INPUT, price)

    def select_category(self):
        self.click(CreationNewAdvertisementLocators.SELECT_CATEGORY_DROPDOWN_BUTTON)
        self.click(CreationNewAdvertisementLocators.GARDEN_CHOICE)

    def select_city(self):
        self.click(CreationNewAdvertisementLocators.SELECT_CITY_DROPDOWN_BUTTON)
        self.click(CreationNewAdvertisementLocators.EKB_CITY_CHOICE)

    def publish_advertisement(self):
        self.click(CreationNewAdvertisementLocators.PUBLISH_AD_BUTTON)