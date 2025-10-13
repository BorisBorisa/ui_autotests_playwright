import allure

from playwright.sync_api import Page

from components.base_component import BaseComponent

from elements.text import Text
from elements.button import Button


class RemoveDialogComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.close_icon_button = Button(page, '//*[@role="dialog"]/button', "close icon")

        self.title = Text(page, '//*[@data-slot="dialog-title"]', "title")
        self.description = Text(page, '//*[@data-slot="dialog-description"]', "description")

        self.close_button = Button(page, '//button[text()="Close"]', "close")
        self.remove_button = Button(page, '//button[text()="Remove"]', "remove")

    @allure.step('Check that remove dialog visible')
    def check_visible(self):
        self.close_icon_button.check_visible()

        self.title.check_visible()
        self.title.check_have_text("Are you absolutely sure?")

        self.description.check_visible()
        self.description.check_have_text(
            "This action cannot be undone. This will permanently delete your item from your cart."
        )

        self.close_button.check_visible()
        self.remove_button.check_visible()

    @allure.step('Click close dialog icon')
    def click_close_icon_button(self):
        self.close_icon_button.click()

    @allure.step('Click close dialog button')
    def click_close_button(self):
        self.close_button.click()

    @allure.step('Click confirm remove button')
    def click_remove_button(self):
        self.remove_button.click()
