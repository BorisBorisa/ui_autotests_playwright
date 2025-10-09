from playwright.async_api import Page

from pages.base_page import BasePage

from components.navigation.auth_header_component import AuthHeaderComponent

from elements.text import Text
from elements.button import Button


class CheckoutCompletePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.header = AuthHeaderComponent(page)
        self.title = Text(page, '//*[@id="checkout-complete"]/h3', "title")

        self.success_message_title = Text(page, '//*[@id="checkout-complete"]/*/h3', "success message title")
        self.success_message = Text(page, '//*[@id="checkout-complete"]/*/p', "success message")

        self.continue_shopping_button = Button(page, '//button/*[text()="Continue Shopping"]', "continue shopping")
