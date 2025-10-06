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
            page, '//*[@data-slot="command-item" and @data-value="asc"]',"ascending order"
        )
        self.descending_order_button = Button(
            page, '//*[@data-slot="command-item" and @data-value="dsc"]',"descending order"
        )
        self.low_to_high_button = Button(
            page, '//*[@data-slot="command-item" and @data-value="low"]',"low to high order"
        )
        self.high_to_low_button = Button(
            page, '//*[@data-slot="command-item" and @data-value="high"]',"high to low order"
        )

    def fill_order_search_input(self, value: str):
        self.menu_button.click()

        expect(self.search_input).to_be_visible()
        self.search_input.fill(value)

    def click_ascending_order(self):
        self.menu_button.click()

        expect(self.ascending_order_button).to_be_visible()
        self.ascending_order_button.click()

    def click_descending_order(self):
        self.menu_button.click()

        expect(self.descending_order_button).to_be_visible()
        self.descending_order_button.click()

    def click_low_to_high_order(self):
        self.menu_button.click()

        expect(self.low_to_high_button).to_be_visible()
        self.low_to_high_button.click()

    def click_high_to_low_order(self):
        self.menu_button.click()

        expect(self.high_to_low_button).to_be_visible()
        self.high_to_low_button.click()