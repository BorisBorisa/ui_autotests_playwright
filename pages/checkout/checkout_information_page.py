import allure

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

    def is_page_opened(self):
        self.title.check_visible()
        self.title.check_have_text("Checkout: Your Information")

    @allure.step("Click cancel button")
    def click_cancel_button(self):
        self.cancel_button.click()

    @allure.step("Click continue button")
    def click_continue_button(self):
        self.continue_button.click()

    @allure.step("Fill checkout information form")
    def fill_checkout_information_form(self, first_name: str, last_name: str, zip_code: str):
        self.checkout_information_form.fill(
            first_name=first_name,
            last_name=last_name,
            zip_code=zip_code
        )

    @allure.step("Check visible checkout information form")
    def check_visible_checkout_information_form(self, email: str, first_name: str, last_name: str, zip_code: str):
        self.checkout_information_form.check_visible(
            email=email,
            first_name=first_name,
            last_name=last_name,
            zip_code=zip_code
        )
