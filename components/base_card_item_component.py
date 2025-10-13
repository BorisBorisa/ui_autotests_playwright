import allure

from components.base_component import BaseComponent

from playwright.sync_api import Page

from elements.text import Text
from elements.button import Button
from elements.image import Image


class BaseCardItemComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.image = Image(page, '//*[contains(@class, "cart-list")]//img', "product")
        self.name = Text(page, '//*[contains(@class, "cart-list")]//h3', "product name")
        self.remove_button = Button(page, '//button[text()="Remove"]', "product remove")

        self.price = Text(page, '//*[text()="Price"]/following-sibling::*', "price")
        self.total_price = Text(page, '//*[text()="Total"]/following-sibling::*', "total price")

    @allure.step('Check card item visible')
    def check_visible(self, name: str, nth: int = 0, **kwargs):
        self.image.check_visible(nth, **kwargs)

        self.name.check_visible(nth, **kwargs)
        self.name.check_have_text(name, nth, **kwargs)

        self.remove_button.check_visible(nth, **kwargs)

        self.price.check_visible(nth, **kwargs)
        self.total_price.check_visible(nth, **kwargs)

    @allure.step("Getting product price")
    def get_price(self, nth: int = 0, **kwargs) -> float:
        price = self.price.get_inner_text(nth, **kwargs)
        return float(price.replace("$", ""))

    @allure.step("Getting product total price")
    def get_total_price(self, nth: int = 0, **kwargs) -> float:
        total_price = self.total_price.get_inner_text(nth, **kwargs)
        return float(total_price.replace("$", ""))
