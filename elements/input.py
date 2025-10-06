from playwright.sync_api import expect, Locator
from elements.base_element import BaseElement


class Input(BaseElement):
    @property
    def type_of(self) -> str:
        return "input"

    def fill(self, value: str, nth: int = 0, **kwargs):
        locator = self.get_locator(**kwargs).nth(nth)
        locator.fill(value)

    def check_have_value(self, value: str, nth: int = 0, **kwargs):
        locator = self.get_locator(**kwargs).nth(nth)
        expect(locator).to_have_value(value)
