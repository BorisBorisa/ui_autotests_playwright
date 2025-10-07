from playwright.sync_api import Page

from components.base_component import BaseComponent

from elements.text import Text
from elements.link import Link


class FavoritesEmptyViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.description = Text(page, '//*[@id="favorites-wrapper"]//h2', "favorites empty view description")
        self.continue_shopping_link = Link(page, '//*[@id="favorites-wrapper"]//a', "continue shopping")

    def check_visible(self):
        self.description.check_visible()
        self.description.check_have_text(text="You have no favorite products")

        self.continue_shopping_link.check_visible()
        self.continue_shopping_link.check_have_text(text="Continue Shopping")

    def click_continue_shopping_link(self):
        self.continue_shopping_link.click()
