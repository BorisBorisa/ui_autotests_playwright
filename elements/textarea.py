from playwright.sync_api import Locator, expect

from elements.base_element import BaseElement


class Textarea(BaseElement):
    @property
    def type_of(self) -> str:
        return "textarea"

    def fill(self, value: str, nth: int = 0, **kwargs):
        locator = self.get_locator(**kwargs).nth(nth)
        locator.fill(value)

    def check_value(self, value: str, nth: int = 0, **kwargs):
        locator = self.get_locator(**kwargs).nth(nth)
        expect(locator).to_have_value(value)
