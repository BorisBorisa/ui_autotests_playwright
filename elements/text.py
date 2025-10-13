from elements.base_element import BaseElement


class Text(BaseElement):
    @property
    def type_of(self) -> str:
        return "text"

    def get_inner_text(self, nth: int = 0, **kwargs) -> str:
        locator = self.get_locator(nth, **kwargs)
        return locator.inner_text()
