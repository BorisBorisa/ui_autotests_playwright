import allure

from playwright.sync_api import Page

from components.base_component import BaseComponent

from elements.text import Text
from elements.button import Button


class LogoutDialogComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.close_icon_button = Button(page, '//*[@role="dialog"]/button', "close icon")

        self.title = Text(page, '//*[@data-slot="dialog-title"]', "title")
        self.description = Text(page, '//*[@data-slot="dialog-description"]', "description")

        self.close_button = Button(page, '//*[@role="dialog"]//button[text()="Close"]', "close")
        self.logout_button = Button(page, '//*[@role="dialog"]//button[text()="Logout"]', "logout")

    @allure.step('Check that logout dialog visible')
    def check_visible(self):
        self.close_icon_button.check_visible()

        self.title.check_visible()
        self.title.check_have_text("Are you sure you want to log out?")

        self.description.check_visible()
        self.description.check_have_text("You're about to log out. Continue?")

        self.close_button.check_visible()
        self.logout_button.check_visible()

    @allure.step('Click close dialog icon')
    def click_close_icon_button(self):
        self.close_icon_button.click()

    @allure.step('Click close dialog button')
    def click_close_button(self):
        self.close_button.click()

    @allure.step('Click logout button')
    def click_logout_button(self):
        self.logout_button.click()
