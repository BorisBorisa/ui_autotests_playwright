import allure

from playwright.async_api import Page

from pages.base_page import BasePage

from components.sonner_toast_component import SonnerToastComponent
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

        self.toast_notification = SonnerToastComponent(page)

    def is_page_opened(self):
        self.title.check_visible()
        self.title.check_have_text("Products")

    def click_product_favorite_button(self, index: int = 0, **kwargs):
        self.product_card.favorite_button.click(index, **kwargs)

    def check_product_favorite_button_is_active(self, index: int = 0, **kwargs):
        self.product_card.favorite_button.is_active(index, **kwargs)

    def check_product_favorite_button_is_inactive(self, index: int = 0, **kwargs):
        self.product_card.favorite_button.is_inactive(index, **kwargs)

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

    def check_visible_added_to_favorites_notification(self):
        self.toast_notification.check_visible("success", "Added to favorites")

    def check_visible_remove_from_favorites_notification(self):
        self.toast_notification.check_visible("warning", "Removed from favorites")
