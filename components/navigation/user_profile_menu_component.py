from playwright.sync_api import Page, expect

from components.base_component import BaseComponent


class UserProfileMenuComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.menu_button = page.locator(".profile .user-name")
        self.favorites_menu_button = page.locator('//*[text()="Favorites"]')
        self.log_out_menu_button = page.locator('//*[text()="Log out"]')

    def click_user_favorites(self):
        self.menu_button.click()

        expect(self.favorites_menu_button).to_be_visible()
        self.favorites_menu_button.click()

    def click_user_log_out(self):
        self.menu_button.click()

        expect(self.log_out_menu_button).to_be_visible()
        self.log_out_menu_button.click()
