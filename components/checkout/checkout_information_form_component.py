import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent

from elements.input import Input


class CheckoutInformationFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.email_input = Input(page, '//*[text()="Email"]/parent::*/input', "email")
        self.first_name_input = Input(page, '//*[text()="First Name"]/parent::*/input', "first name")
        self.last_name_input = Input(page, '//*[text()="Last Name"]/parent::*/input', "last name")
        self.zip_code_input = Input(page, '//*[text()="Zip Code"]/parent::*/input', "zip code")

    @allure.step("Fill checkout information form")
    def fill(self, first_name: str, last_name: str, zip_code: str):
        self.first_name_input.fill(first_name)
        self.first_name_input.check_have_value(first_name)

        self.last_name_input.fill(last_name)
        self.last_name_input.check_have_value(last_name)

        self.zip_code_input.fill(zip_code)
        self.zip_code_input.check_have_value(zip_code)

    @allure.step("Check visible checkout information form")
    def check_visible(self, email: str, first_name: str, last_name: str, zip_code: str):
        self.email_input.check_visible()
        self.email_input.check_have_value(email)

        self.first_name_input.check_visible()
        self.first_name_input.check_have_value(first_name)

        self.last_name_input.check_visible()
        self.last_name_input.check_have_value(last_name)

        self.zip_code_input.check_visible()
        self.zip_code_input.check_have_value(zip_code)
