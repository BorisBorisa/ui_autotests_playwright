from playwright.async_api import Page

from pages.base_page import BasePage

from components.navigation.auth_header_component import AuthHeaderComponent
from components.card.card_item_component import CardItemComponent
from components.card.remove_dialog_component import RemoveDialogComponent
from components.card.card_empty_view_component import CardEmptyViewComponent

from elements.text import Text
from elements.button import Button


class CardPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.header = AuthHeaderComponent(page)
        self.title = Text(page, '//*[@id="product-sort"]/h3', "title")

        self.empty_view = CardEmptyViewComponent(page)

        self.card_item = CardItemComponent(page)

        self.remove_dialog = RemoveDialogComponent(page)

        self.continue_shopping_button = Button(page, '//button/*[(text()="Continue Shopping")]', "continue shopping")
        self.checkout_button = Button(page, '//button/*[(text()="Checkout")]', "checkout")
