import allure

from elements.base_element import BaseElement
from tools.logger import get_logger

logger = get_logger("TEXT")


class Text(BaseElement):
    @property
    def type_of(self) -> str:
        return "text"

    def get_inner_text(self, nth: int = 0, **kwargs) -> str:
        locator = self.get_locator(nth, **kwargs)
        step = f'Getting inner text of {self.type_of} "{self.name}"'

        with allure.step(step):
            logger.info(step)
            return locator.inner_text()
