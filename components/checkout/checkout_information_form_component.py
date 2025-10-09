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
