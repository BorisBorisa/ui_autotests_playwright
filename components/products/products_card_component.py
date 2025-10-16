from playwright.sync_api import Page

from components.base_component import BaseComponent

from elements.image import Image
from elements.text import Text
from elements.button import Button
from elements.favorite_radio_button import FavoriteRadioButton

from tools.data_clases import Product


class ProductCardComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.favorite_button = FavoriteRadioButton(
            page, '//*[contains(@class,"products")]//*[@role="button"]/button', "product"
        )
        self.image = Image(page, '//*[contains(@class,"products")]//img', "product")

        self.name = Text(page, '//*[contains(@class,"products")]//a[2]', "name")
        self.description = Text(page, '//*[contains(@class,"products")]//a[3]', "description")
        self.price = Text(page, '//*[text()="$"]', "price")
        self.add_to_card_button = Button(
            page, '//*[contains(@class,"products")]//button[contains(@class, "border")]', "add to card"
        )

    def check_visible(self, name: str, description: str, price: str, nth: int = 0, **kwargs):
        self.favorite_button.check_visible(nth, **kwargs)

        self.image.check_visible(nth, **kwargs)

        self.name.check_visible(nth, **kwargs)
        self.name.check_have_text(name, nth, **kwargs)

        self.description.check_visible(nth, **kwargs)
        self.description.check_have_text(description, nth, **kwargs)

        self.price.check_visible(nth, **kwargs)
        self.price.check_have_text(price, nth, **kwargs)

        self.add_to_card_button.check_visible(nth, **kwargs)

    def click(self, index: int = 0, **kwargs):
        self.image.click(index, **kwargs)

    def click_favorite_button(self, index: int = 0, **kwargs):
        self.favorite_button.click(index, **kwargs)

    def click_add_to_card_button(self, index: int = 0, **kwargs):
        self.add_to_card_button.click(index, **kwargs)

    def check_add_to_cart_button_in_remove_state(self, nth: int = 0, **kwargs):
        self.add_to_card_button.check_have_text("Remove from cart", nth, **kwargs)

    def check_add_to_cart_button_in_add_state(self, nth: int = 0, **kwargs):
        self.add_to_card_button.check_have_text("Add to cart", nth, **kwargs)

    def check_favorite_button_is_active(self, index: int = 0, **kwargs):
        self.favorite_button.is_active(index, **kwargs)

    def check_favorite_button_is_inactive(self, index: int = 0, **kwargs):
        self.favorite_button.is_inactive(index, **kwargs)

    def _count_products_by_name(self, **kwargs) -> int:
        locator = self.page.locator(self.name.locator.format(**kwargs))
        return locator.count()

    def get_all_prices(self, **kwargs) -> list[float]:
        prices = []

        for nth in range(self._count_products_by_name()):
            price = self.price.get_inner_text(nth, **kwargs)
            prices.append(float(price.replace("$", "")))

        return prices

    def get_all_names(self, **kwargs):
        return [self.name.get_inner_text(i, **kwargs) for i in range(self._count_products_by_name())]

    def get_product(self, nth: int = 0, **kwargs) -> Product:
        return Product(
            name=self.name.get_inner_text(nth, **kwargs),
            img_src=self.image.get_src(nth, **kwargs),
            price=self.price.get_inner_text()
        )

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
