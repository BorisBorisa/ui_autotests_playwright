from re import Pattern

import allure
from playwright.sync_api import Page, expect


class BaseComponent:
    def __init__(self, page: Page):
        self.page = page

    def check_current_url(self, expected_url: str | Pattern[str]):
        if isinstance(expected_url, Pattern):
            step = f"Checking that current URL matches pattern '{expected_url.pattern}'"
        else:
            step = f"Checking that current URL equals '{expected_url}'"

        with allure.step(step):
            expect(self.page).to_have_url(expected_url)
