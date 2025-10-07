from elements.base_element import BaseElement
from playwright.sync_api import expect


class FavoriteRadioButton(BaseElement):
    @property
    def type_of(self) -> str:
        return "favorite radio button"

    def is_active(self, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        expect(locator).to_have_attribute("style", "color: rgb(255, 0, 0);")
