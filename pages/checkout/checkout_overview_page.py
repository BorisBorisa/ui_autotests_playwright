from playwright.async_api import Page

from pages.base_page import BasePage

from components.navigation.auth_header_component import AuthHeaderComponent
from components.card.base_card_item_component import BaseCardItemComponent

from elements.text import Text
from elements.button import Button


class CheckoutOverviewPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.header = AuthHeaderComponent(page)
        self.title = Text(page, '//*[@id="checkout-overview"]/h3', "title")

        self.card_item = BaseCardItemComponent(page)

        self.payment_info_text = Text(page, '//h4[contains(text(), "Payment Information")]/parent::*/p', "")
        self.shipping_info_text = Text(page, '//h4[contains(text(), "Shipping Information")]/parent::*/p', "")

        self.items_price = Text(page, '//h4[contains(text(), "Price Total")]/parent::*/p[1]', "")
        self.tax = Text(page, '//h4[contains(text(), "Price Total")]/parent::*/p[2]', "")
        self.total_price = Text(page, '//h4[contains(text(), "Price Total")]/parent::*/p[3]', "")

        self.cancel_button = Button(page, '//button/*[text()="Cancel"]', "cancel")
        self.finish_button = Button(page, '//button/*[text()="Finish"]', "finish")

    def get_items_price(self) -> float:
        text = self.items_price.get_text()
        return float(text.split("$")[1])

    def get_tax(self) -> float:
        text = self.tax.get_text()
        return float(text.split("$")[1])

    def get_total_price(self) -> float:
        text = self.total_price.get_text()
        return float(text.split("$")[1])
