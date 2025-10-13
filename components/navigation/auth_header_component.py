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

    @allure.step('Get cart items count')
    def get_cart_count(self, nth: int = 0, **kwargs) -> int:
        try:
            self.cart_button_counter.check_visible(nth, **kwargs)
            count = self.cart_button_counter.get_inner_text(nth, **kwargs)
            return int(count)
        except AssertionError:
            return 0
