from playwright.sync_api import Page

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

        self.ascending_order_button.check_visible()

        with self.page.expect_response(lambda r: "?order_by=asc" in r.url and r.status == 200):
            self.ascending_order_button.click()

        self.menu_button.check_have_text("A to Z (Ascending)")

    def click_descending_order(self):
        self.menu_button.click()

        self.descending_order_button.check_visible()

        with self.page.expect_response(lambda r: "?order_by=dsc" in r.url and r.status == 200):
            self.descending_order_button.click()

        self.menu_button.check_have_text("Z to A (Descending)")

    def click_low_to_high_order(self):
        self.menu_button.click()

        self.low_to_high_button.check_visible()

        with self.page.expect_response(lambda r: "?order_by=low" in r.url and r.status == 200):
            self.low_to_high_button.click()

        self.menu_button.check_have_text("Low to High (Price)")

    def click_high_to_low_order(self):
        self.menu_button.click()

        self.high_to_low_button.check_visible()

        with self.page.expect_response(lambda r: "?order_by=high" in r.url and r.status == 200):
            self.high_to_low_button.click()

        self.menu_button.check_have_text("High to Low (Price)")
