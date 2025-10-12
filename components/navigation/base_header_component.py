from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.link import Link


class BaseHeaderComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.logo_link = Link(page, '//*[@id="ecommerce-header"]//a', "logo")

    def click_logo_link(self):
        self.logo_link.click()
