from playwright.async_api import Page

from pages.base_page import BasePage

from components.navigation.auth_header_component import AuthHeaderComponent
from components.checkout.checkout_information_form_component import CheckoutInformationFormComponent

from elements.text import Text
from elements.button import Button


class CheckoutInformationPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.header = AuthHeaderComponent(page)
        self.title = Text(page, '//*[@id="checkout-info"]/h3', "title")

        self.checkout_information_form = CheckoutInformationFormComponent(page)

        self.cancel_button = Button(page, '//button/*[text()="Cancel"]', "cancel")
        self.continue_button = Button(page, '//button/*[text()="Continue"]', "continue")