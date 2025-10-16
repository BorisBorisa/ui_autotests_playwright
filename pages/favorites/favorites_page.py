import allure

from playwright.async_api import Page

from pages.base_page import BasePage

from components.sonner_toast_component import SonnerToastComponent
from components.navigation.auth_header_component import AuthHeaderComponent
from components.favorites.favorites_empty_view_component import FavoritesEmptyViewComponent
from components.products.products_order_menu_component import ProductsOrderMenuComponent
from components.products.products_card_component import ProductCardComponent

from elements.text import Text

from tools.data_clases import Product


class FavoritesPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.header = AuthHeaderComponent(page)
        self.title = Text(page, '//*[@id="product-sort"]/h3', "title")

        self.products_order_menu = ProductsOrderMenuComponent(page)
        self.product_card = ProductCardComponent(page)

        self.toast_notification = SonnerToastComponent(page)

        self.empty_view = FavoritesEmptyViewComponent(page)

    def is_page_opened(self):
        self.title.check_visible()
        self.title.check_have_text("Favorites")

    def click_product_favorite_button(self, index: int = 0):
        self.product_card.favorite_button.click(index)

    def check_favorites_products_equals_expected(self, expected_products: list[Product]):
        actual_products = self.product_card.get_all_products()

        expected_sorted = sorted(expected_products)
        actual_sorted = sorted(actual_products)

        with allure.step("Verify that favorite products match the expected ones"):
            assert expected_sorted == actual_sorted, f"Expected: {expected_sorted}\nActual: {actual_sorted}"
