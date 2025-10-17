import allure

from playwright.sync_api import Page

from components.base_component import BaseComponent

from elements.text import Text
from elements.image import Image

from tools.data_clases import Product


class BaseCardItemComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.image = Image(page, '//*[contains(@class, "cart-list")]//img', "product")
        self.name = Text(page, '//*[contains(@class, "cart-list")]//h3', "product name")

        self.quantity = Text(page, '//*[text()="Quantity"]/following-sibling::*/span', "quantity")

        self.price = Text(page, '//*[text()="Price"]/following-sibling::*', "price")
        self.total_price = Text(page, '//*[text()="Total"]/following-sibling::*', "total price")

    @allure.step("Check cart item {index} is visible")
    def check_visible(self, product: Product, index: int = 0):
        self.image.check_visible(index)
        self.image.check_image_src(product.img_src, index)

        self.name.check_visible(index)
        self.name.check_have_text(product.name, index)

        self.quantity.check_visible(index)

        self.price.check_visible(index)
        self.price.check_have_text(product.price, index)

        self.total_price.check_visible(index)

    @allure.step("Check that cart items match expected products list")
    def check_cart_items_equal_expected(self, expected_products: list[Product]):
        for index, product in enumerate(expected_products):
            self.check_visible(product, index)
