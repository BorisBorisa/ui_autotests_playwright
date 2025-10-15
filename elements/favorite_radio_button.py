import allure

from elements.base_element import BaseElement
from playwright.sync_api import expect
from tools.logger import get_logger

logger = get_logger("FAVORITE_RADIO_BUTTON")


class FavoriteRadioButton(BaseElement):
    @property
    def type_of(self) -> str:
        return "favorite radio button"

    def _check_active_state(self, active: bool = True, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        state = "active" if active else "inactive"
        color = "rgb(255, 0, 0)" if active else "rgb(34, 34, 34)"
        step = f'Checking that {self.type_of} "{self.name}" is {state}'

        with allure.step(step):
            logger.info(step)
            expect(locator).to_have_attribute("style", f"color: {color};")

    def is_active(self, nth: int = 0, **kwargs):
        self._check_active_state(True, nth, **kwargs)

    def is_inactive(self, nth: int = 0, **kwargs):
        self._check_active_state(False, nth, **kwargs)
