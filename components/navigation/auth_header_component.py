import allure
from playwright.sync_api import Page

from components.navigation.base_header_component import BaseHeaderComponent
from components.navigation.user_profile_menu_component import UserProfileMenuComponent

from elements.button import Button
from elements.text import Text


class AuthHeaderComponent(BaseHeaderComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.cart_button = Button(page, '//*[@id="ecommerce-header"]//*[@role="button"]', "card")
        self.cart_button_counter = Text(page, '//*[@id="ecommerce-header"]//*[@role="button"]//*[text()]',
                                        "card counter")

        self.user_profile_menu = UserProfileMenuComponent(page)

    @allure.step('Check header visible')
    def check_visible(self, email: str):
        self.logo_link.check_visible()
        self.cart_button.check_visible()
        self.user_profile_menu.check_visible(email)

    @allure.step("Clicking cart button")
    def click_cart_button(self):
        self.cart_button.click()

    def click_user_favorites(self):
        self.user_profile_menu.click_user_favorites()

    def click_user_log_out(self):
        self.click_user_log_out()

    @allure.step("Check cart counter value")
    def check_cart_counter_value(self, expected_value: int):
        self.cart_button_counter.check_have_text(str(expected_value))
