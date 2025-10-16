import allure

from playwright.sync_api import Page

from components.base_component import BaseComponent

from elements.text import Text
from elements.button import Button


class CardEmptyViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.description = Text(page, '//*[@id="cart"]//h1', "card empty view description")
        self.continue_shopping_button = Button(page, '//*[@id="cart"]//button', "continue shopping")

    @allure.step('Check visible card empty view')
    def check_visible(self):
        self.description.check_visible()
        self.description.check_have_text(text="Your cart is empty.")

        self.continue_shopping_button.check_visible()
        self.continue_shopping_button.check_have_text(text="Continue Shopping")

    @allure.step('Click continue shopping button')
    def click_continue_shopping_button(self):
        self.continue_shopping_button.click()
