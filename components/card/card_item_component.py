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

    @allure.step("Check cart item {index} is visible")
    def check_visible(self, product: Product, index: int = 0):
        super().check_visible(product, index)

        self.quantity_decrease_button.check_visible(index)
        self.quantity_increase_button.check_visible(index)

    @allure.step("Click remove button on cart item {index}")
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
