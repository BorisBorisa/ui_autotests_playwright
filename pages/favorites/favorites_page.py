from playwright.async_api import Page

from components.favorites.favorites_empty_view_component import FavoritesEmptyViewComponent
from pages.base_page import BasePage

from components.navigation.auth_header_component import AuthHeaderComponent
from components.products.products_order_menu_component import ProductsOrderMenuComponent


from elements.text import Text


class FavoritesPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.header = AuthHeaderComponent(page)
        self.title = Text(page, '//*[@id="product-sort"]/h3', "title")

        self.products_order_menu = ProductsOrderMenuComponent(page)

        self.empty_view = FavoritesEmptyViewComponent(page)