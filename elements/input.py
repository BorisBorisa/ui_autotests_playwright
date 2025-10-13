import allure

from playwright.sync_api import expect
from elements.base_element import BaseElement


class Input(BaseElement):
    @property
    def type_of(self) -> str:
        return "input"

    def fill(self, value: str, nth: int = 0, **kwargs):
        locator = self.get_locator(**kwargs).nth(nth)
        step = f'Fill {self.type_of} "{self.name}" to value "{value}"'

        with allure.step(step):
            locator.fill(value)

    def check_have_value(self, value: str, nth: int = 0, **kwargs):
        locator = self.get_locator(**kwargs).nth(nth)
        step = f'Checking that {self.type_of} "{self.name}" has a value "{value}"'

        with allure.step(step):
            expect(locator).to_have_value(value)
