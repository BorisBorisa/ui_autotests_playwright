import allure

from playwright.async_api import Page
from pages.base_page import BasePage

from components.navigation.auth_header_component import AuthHeaderComponent
from components.products.products_order_menu_component import ProductsOrderMenuComponent
from components.products.products_card_component import ProductCardComponent

from elements.text import Text


class ProductsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.header = AuthHeaderComponent(page)
        self.title = Text(page, '//*[@id="product-sort"]/h3', "title")

        self.products_order_menu = ProductsOrderMenuComponent(page)
        self.product_card = ProductCardComponent(page)

    def is_page_opened(self):
        self.title.check_visible()

    @allure.step("Check prices sorted low to high")
    def check_prices_sorted_low_to_high(self):
        prices = self.product_card.get_all_prices()
        assert prices == sorted(prices), f"Product prices are not sorted from low to high: {prices}"

    @allure.step("Check prices sorted high to low")
    def check_prices_sorted_high_to_low(self):
        prices = self.product_card.get_all_prices()
        assert prices == sorted(prices, reverse=True), f"Product prices are not sorted from high to low: {prices}"

    @allure.step("Check prices sorted a to z")
    def check_names_sorted_a_to_z(self):
        names = self.product_card.get_all_names()
        assert names == sorted(names), f"Product names are not sorted alphabetically A → Z: {names}"

    @allure.step("Check prices sorted z to a")
    def check_names_sorted_z_to_a(self):
        names = self.product_card.get_all_names()
        assert names == sorted(names, reverse=True), f"Product names are not sorted alphabetically Z → A: {names}"
