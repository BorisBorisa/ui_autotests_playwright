import allure
from playwright.sync_api import Page, expect

from components.base_component import BaseComponent

from elements.button import Button


class UserProfileMenuComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.menu_button = Button(page, ".profile .user-name", "menu")
        self.favorites_menu_button = Button(page, '//*[text()="Favorites"]', "favorites")
        self.log_out_menu_button = Button(page, '//*[text()="Log out"]', "log out")

    @allure.step("Check visible user profile menu button")
    def check_visible(self, email: str):
        self.menu_button.check_visible()
        self.menu_button.check_have_text(email)

    @allure.step("Click user favorites button")
    def click_user_favorites(self):
        self.menu_button.click()

        self.favorites_menu_button.check_visible()
        self.favorites_menu_button.click()

    @allure.step("Click user log out button")
    def click_user_log_out(self):
        self.menu_button.click()

        self.log_out_menu_button.check_visible()
        self.log_out_menu_button.click()
