import allure

from playwright.sync_api import Page

from components.card.base_card_item_component import BaseCardItemComponent
from components.card.remove_dialog_component import RemoveDialogComponent

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

        self.remove_dialog = RemoveDialogComponent(page)

    @allure.step('Check card item visible')
    def check_visible(self, name: str, index: int = 0):
        super().check_visible(name, index)

        self.quantity_decrease_button.check_visible(index)
        self.quantity_increase_button.check_visible(index)
        self.quantity.check_visible(index)

    def check_quantity_equals_expected(self, expected_quantity: int, index: int = 0):
        self.quantity.check_have_text(str(expected_quantity), index)

    def check_price_equal_expected(self, price: str, index: int = 0):
        self.price.check_have_text(price, index)

    def check_total_price_equal_expected(self, price: str, quantity: int, index: int = 0):
        expected_total_price = float(price.replace("$", "")) * quantity

        self.total_price.check_have_text(f"${expected_total_price:.2f}", index)

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
