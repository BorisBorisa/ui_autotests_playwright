from playwright.sync_api import expect
from elements.base_element import BaseElement


class Image(BaseElement):
    @property
    def type_of(self) -> str:
        return "image"

    def get_src(self, nth: int = 0, **kwargs) -> str:
        locator = self.get_locator(nth, **kwargs)
        return locator.get_attribute("src")

    def check_image_src(self, src: str, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        expect(locator).to_have_attribute("src", src)
