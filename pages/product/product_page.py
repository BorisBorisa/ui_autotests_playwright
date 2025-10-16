from playwright.async_api import Page

from pages.base_page import BasePage

from components.navigation.auth_header_component import AuthHeaderComponent
from components.sonner_toast_component import SonnerToastComponent

from elements.favorite_radio_button import FavoriteRadioButton
from elements.input import Input
from elements.text import Text
from elements.image import Image
from elements.button import Button

from tools.data_clases import Product


class ProductPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.header = AuthHeaderComponent(page)

        self.back_to_products_button = Button(page, '//button[text()="Back to Products"]', "back to products")

        self.image = Image(page, '//*[@class="product-details-wrapper"]//img', "product")
        self.favorite_button = FavoriteRadioButton(
            page, '//*[@class="product-details-wrapper"]//*[@role="button"]/button', "product"
        )

        self.name = Text(page, '//*[@class="product-details-wrapper"]//h1', "name")
        self.description = Text(page, '//*[@class="product-details-wrapper"]//p', "description")

        self.quantity_decrease_button = Button(page, '//button[text()="−"]', "decrease")
        self.quantity_increase_button = Button(page, '//button[text()="+"]', "increase")
        self.quantity = Input(page, '//*[@class="product-details-wrapper"]//input', "quantity")

        self.price = Text(page, '//*[text()="$"]', "test")

        self.add_to_card_button = Button(page, '//*[@class="add-cart"]/button', "add to card")

        self.toast_notification = SonnerToastComponent(page)

    def is_page_opened(self):
        self.back_to_products_button.check_visible()
        self.back_to_products_button.check_have_text("Back to Products")

    def click_back_to_product_button(self):
        self.back_to_products_button.click()

    def click_product_favorite_button(self, **kwargs):
        self.favorite_button.click(**kwargs)

    def check_product_favorite_button_is_active(self, **kwargs):
        self.favorite_button.is_active(**kwargs)

    def check_product_favorite_button_is_inactive(self, **kwargs):
        self.favorite_button.is_inactive(**kwargs)

    def get_product(self, **kwargs) -> Product:
        return Product(
            name=self.name.get_inner_text(**kwargs),
            description=self.description.get_inner_text(**kwargs),
            img_src=self.image.get_src(**kwargs),
            price=self.price.get_inner_text()
        )
