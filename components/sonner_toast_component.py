import allure
from playwright.sync_api import Page
from typing import Literal

from components.base_component import BaseComponent

from elements.text import Text


class SonnerToastComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.sonner_toast = Text(
            page, '//*[@data-sonner-toast and @data-type="{toast_type}"]//*[@data-title]', "sonner toast"
        )

    @allure.step("Check sonner toast notification visible")
    def check_visible(
            self,
            toast_type: Literal['default', 'success', 'info', 'warning', 'error'],
            text: str
    ):
        self.sonner_toast.check_visible(toast_type=toast_type)
        self.sonner_toast.check_have_text(text=text, toast_type=toast_type)

    def check_visible_added_to_favorites_notification(self):
        self.check_visible("success", "Added to favorites")

    def check_visible_remove_from_favorites_notification(self):
        self.check_visible("warning", "Removed from favorites")
