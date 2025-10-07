from playwright.sync_api import Page

from components.navigation.base_header_component import BaseHeaderComponent
from components.navigation.user_profile_menu_component import UserProfileMenuComponent

from elements.button import Button
from elements.text import Text


class AuthHeaderComponent(BaseHeaderComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.card_button = Button(page, '//*[@id="ecommerce-header"]//*[@role="button"]', "card")
        self.card_button_counter = Text(page, '//*[@id="ecommerce-header"]//*[@role="button"]//*[text()]',
                                        "card counter")

        self.user_profile_menu = UserProfileMenuComponent(page)

    def check_visible(self):
        self.card_button.check_visible()

    def get_card_count(self, nth: int = 0, **kwargs) -> int:
        try:
            self.card_button_counter.check_visible(nth, **kwargs)
            count = self.card_button_counter.get_text(nth, **kwargs)
            return int(count)
        except AssertionError:
            return 0
