import allure

from playwright.sync_api import Page

from components.base_card_item_component import BaseCardItemComponent

from elements.text import Text
from elements.button import Button


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
