from playwright.async_api import Page

from elements.favorite_radio_button import FavoriteRadioButton
from elements.input import Input
from pages.base_page import BasePage

from elements.text import Text
from elements.image import Image
from elements.button import Button


class ProductPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.back_to_products_button = Button(page, '//button[text()="Back to Products"]', "back to products")

        self.image = Image(page, '//*[@class="product-details-wrapper"]//img', "product")
        self.favorite_button = FavoriteRadioButton(
            page, '//*[@class="product-details-wrapper"]//*[@role="button"]/button', "product"
        )

        self.name = Text(page, '//*[@class="product-details-wrapper"]//h1', "name")
        self.description_text = Text(page, '//*[@class="product-details-wrapper"]//p', "description")

        self.quantity_decrease_button = Button(page, '//button[text()="−"]', "decrease")
        self.quantity_increase_button = Button(page, '//button[text()="+"]', "increase")
        self.quantity = Input(page, '//*[@class="product-details-wrapper"]//input', "quantity")

        self.price = Text(page, '//*[text()="$"]', "test")

        self.add_to_card_button = Button(page, '//*[@class="add-cart"]/button', "add to card")

    def click_back_to_product_button(self):
        self.back_to_products_button.click()
