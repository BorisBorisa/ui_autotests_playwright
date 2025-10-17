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

        self.payment_info_text = Text(
            page, '//h4[contains(text(), "Payment Information")]/parent::*/p', "payment information"
        )
        self.shipping_info_text = Text(
            page, '//h4[contains(text(), "Shipping Information")]/parent::*/p', "shipping information"
        )
        self.items_price = Text(page, '//h4[contains(text(), "Price Total")]/parent::*/p[1]', "items price")
        self.tax = Text(page, '//h4[contains(text(), "Price Total")]/parent::*/p[2]', "tax")
        self.total_price = Text(page, '//h4[contains(text(), "Price Total")]/parent::*/p[3]', "total price")

        self.cancel_button = Button(page, '//button/*[text()="Cancel"]', "cancel")
        self.finish_button = Button(page, '//button/*[text()="Finish"]', "finish")

    def is_page_opened(self):
        self.title.check_visible()
        self.title.check_have_text("Checkout: Overview")

    def click_finish_button(self):
        self.finish_button.click()

    def click_cancel_button(self):
        self.cancel_button.click()

    def check_visible_checkout_summary(self):
        self.payment_info_text.check_visible()
        self.shipping_info_text.check_visible()
        self.items_price.check_visible()
        self.tax.check_visible()
        self.total_price.check_visible()

