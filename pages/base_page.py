import allure

from re import Pattern

from playwright.sync_api import Page, expect


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def visit(self, url: str):
        step = f"Opening the url '{url}'"

        with allure.step(step):
            self.page.goto(url, wait_until='networkidle')

    def reload(self):
        step = f"Reloading page with url '{self.page.url}'"

        with allure.step(step):
            self.page.reload(wait_until='networkidle')

    def check_current_url(self, expected_url: str | Pattern[str]):
        if isinstance(expected_url, Pattern):
            step = f"Checking that current URL matches pattern '{expected_url.pattern}'"
        else:
            step = f"Checking that current URL equals '{expected_url}'"

        with allure.step(step):
            expect(self.page).to_have_url(expected_url)
