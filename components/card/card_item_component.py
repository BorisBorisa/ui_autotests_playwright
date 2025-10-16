import allure

from playwright.sync_api import Page

from components.base_card_item_component import BaseCardItemComponent
from components.card.remove_dialog_component import RemoveDialogComponent

from elements.text import Text
from elements.button import Button

from tools.data_clases import Product


class CardItemComponent(BaseCardItemComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.remove_button = Button(page, '//button[text()="Remove"]', "product remove")

        self.quantity_decrease_button = Button(
            page, '//*[text()="Quantity"]/following-sibling::*/*[text()="-"]', "decrease"
        )
        self.quantity_increase_button = Button(
            page, '//*[text()="Quantity"]/following-sibling::*/*[text()="+"]', "increase"
        )
        self.quantity = Text(page, '//*[text()="Quantity"]/following-sibling::*/span', "quantity")

        self.remove_dialog = RemoveDialogComponent(page)

    @allure.step('Check card item visible')
    def check_visible(self, name: str, nth: int = 0):
        super().check_visible(name, nth)

        self.quantity_decrease_button.check_visible(nth)
        self.quantity_increase_button.check_visible(nth)
        self.quantity.check_visible(nth)

    def click_remove_button(self, index: int = 0):
        self.remove_button.click(index)

    def _count_products_by_name(self) -> int:
        locator = self.page.locator(self.name.locator.format())
        return locator.count()

    def get_all_products(self) -> list[Product]:
        products = []

        for nth in range(self._count_products_by_name()):
            product = Product(
                name=self.name.get_inner_text(nth),
                img_src=self.image.get_src(nth),
                price=self.price.get_inner_text(nth)
            )
            products.append(product)

        return products
