import allure

from playwright.sync_api import Page

from components.base_card_item_component import BaseCardItemComponent

from elements.text import Text
from elements.button import Button

from tools.data_clases import Product


class CardItemComponent(BaseCardItemComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.quantity_decrease_button = Button(
            page, '//*[text()="Quantity"]/following-sibling::*/*[text()="-"]', "decrease"
        )
        self.quantity_increase_button = Button(
            page, '//*[text()="Quantity"]/following-sibling::*/*[text()="+"]', "increase"
        )
        self.quantity = Text(page, '//*[text()="Quantity"]/following-sibling::*/span', "quantity")

    @allure.step('Check card item visible')
    def check_visible(self, name: str, nth: int = 0, **kwargs):
        super().check_visible(name, nth, **kwargs)

        self.quantity_decrease_button.check_visible(nth, **kwargs)
        self.quantity_increase_button.check_visible(nth, **kwargs)
        self.quantity.check_visible(nth, **kwargs)

    def _count_products_by_name(self, **kwargs) -> int:
        locator = self.page.locator(self.name.locator.format(**kwargs))
        return locator.count()

    def get_all_products(self, **kwargs) -> list[Product]:
        products = []

        for nth in range(self._count_products_by_name()):
            product = Product(
                name=self.name.get_inner_text(nth, **kwargs),
                img_src=self.image.get_src(nth, **kwargs),
                price=self.price.get_inner_text()
            )
            products.append(product)

        return products
