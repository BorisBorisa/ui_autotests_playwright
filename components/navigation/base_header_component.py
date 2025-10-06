from playwright.sync_api import Page

from components.base_component import BaseComponent


class BaseHeaderComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.logo_link = page.locator('//*[@id="ecommerce-header"]//a')

    def click_logo_link(self):
        self.logo_link.click()
