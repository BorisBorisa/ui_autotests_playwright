from playwright.async_api import Page

from components.base_component import BaseComponent

from elements.image import Image
from elements.text import Text
from elements.button import Button
from elements.favorite_radio_button import FavoriteRadioButton


class ProductCardComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.favorite_button = FavoriteRadioButton(
            page, '//*[contains(@class,"products")]//*[@role="button"]/button', "product"
        )
        self.image = Image(page, '//*[contains(@class,"products")]//img', "product")

        self.name_text = Text(page, '//*[contains(@class,"products")]//a[2]', "name")
        self.description_text = Text(page, '//*[contains(@class,"products")]//a[3]', "description")
        self.price = Text(page, '//*[text()="$"]', "test")
        self.add_to_card_button = Button(page, '//*[contains(@class,"products")]//button[contains(@class, "border")]',
                                         "add to card")

    def check_visible(self, name: str, description: str, price: str, nth: int = 0, **kwargs):
        self.favorite_button.check_visible(nth, **kwargs)

        self.image.check_visible(nth, **kwargs)

        self.name_text.check_visible(nth, **kwargs)
        self.name_text.check_have_text(name, nth, **kwargs)

        self.description_text.check_visible(nth, **kwargs)
        self.description_text.check_have_text(description, nth, **kwargs)

        self.price.check_visible(nth, **kwargs)
        self.price.check_have_text(price, nth, **kwargs)

        self.add_to_card_button.check_visible(nth, **kwargs)

    def get_price(self, nth: int = 0, **kwargs) -> float:
        price = self.price.get_text(nth, **kwargs)
        return float(price.replace("$", ""))
