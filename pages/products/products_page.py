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
