from playwright.sync_api import Page, expect

from components.base_component import BaseComponent

from elements.button import Button
from elements.input import Input


class ProductsOrderMenuComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.menu_button = Button(page, '//*[@id="product-sort"]//button', "order")
        self.search_input = Input(page, '//input[@data-slot="command-input"]', "search")

        self.ascending_order_button = Button(
            page, '//*[@data-slot="command-item" and @data-value="asc"]', "ascending order"
        )
        self.descending_order_button = Button(
            page, '//*[@data-slot="command-item" and @data-value="dsc"]', "descending order"
        )
        self.low_to_high_button = Button(
            page, '//*[@data-slot="command-item" and @data-value="low"]', "low to high order"
        )
        self.high_to_low_button = Button(
            page, '//*[@data-slot="command-item" and @data-value="high"]', "high to low order"
        )

    def check_visible(self):
        self.menu_button.check_visible()

    def fill_order_search_input(self, value: str):
        self.menu_button.click()

        self.search_input.check_visible()
        self.search_input.fill(value)

    def click_ascending_order(self):
        self.menu_button.click()

        self.ascending_order_button.click()
        self.ascending_order_button.check_visible()


    def click_descending_order(self):
        self.menu_button.click()

        self.descending_order_button.click()
        self.descending_order_button.check_visible()


    def click_low_to_high_order(self):
        self.menu_button.click()

        self.low_to_high_button.click()
        self.low_to_high_button.check_visible()


    def click_high_to_low_order(self):
        self.menu_button.click()

        self.high_to_low_button.click()
        self.high_to_low_button.check_visible()

