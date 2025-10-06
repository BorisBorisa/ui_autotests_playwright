from playwright.sync_api import Page

from components.navigation.base_header_component import BaseHeaderComponent
from components.navigation.user_profile_menu_component import UserProfileMenuComponent


class AuthHeaderComponent(BaseHeaderComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.card_button = page.locator('//*[@id="ecommerce-header"]//*[@role="button"]')
        self.card_button_counter = page.locator('//*[@id="ecommerce-header"]//*[@role="button"]//*[text()]')
        self.user_profile_menu = UserProfileMenuComponent(page)
