import allure
from playwright.async_api import Page

from pages.base_page import BasePage

from components.sonner_toast_component import SonnerToastComponent
from components.navigation.base_header_component import BaseHeaderComponent

from elements.text import Text
from elements.input import Input
from elements.button import Button
from elements.link import Link


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.header = BaseHeaderComponent(page)

        self.email_input = Input(page, '//*[@id="email"]', "email")
        self.password_input = Input(page, '//*[@id="password"]', "password")
        self.login_button = Button(page, '//button[text()="Login"]', "login")

        self.email_alert = Text(page, '//*[label[@for="email"]]//p[contains(@class, "text-red-500")]', "email alert")
        self.password_alert = Text(page, '//*[label[@for="password"]]//p[contains(@class, "text-red-500")]',
                                   "password alert")

        self.back_to_home_link = Link(page, '//a[text()="Back to home"]', "back to home")
        self.toast_notification = SonnerToastComponent(page)

    @allure.step("Fill login form")
    def fill_login_form(self, email: str, password: str):
        self.email_input.fill(email)
        self.email_input.check_have_value(email)

        self.password_input.fill(password)
        self.password_input.check_have_value(password)

    def click_login_button(self):
        self.login_button.click()

    def click_back_to_home_link(self):
        self.back_to_home_link.click()

    @allure.step("Check visible wrong email alert")
    def check_visible_wrong_email_alert(self):
        self.email_alert.check_visible()
        self.email_alert.check_have_text("Username is incorrect.")

    @allure.step("Check visible empty email alert")
    def check_visible_empty_email_alert(self):
        self.email_alert.check_visible()
        self.email_alert.check_have_text("Email is a required field")

    @allure.step("Check visible wrong password alert")
    def check_visible_wrong_password_alert(self):
        self.password_alert.check_visible()
        self.password_alert.check_have_text("Password is incorrect.")

    @allure.step("Check visible empty password alert")
    def check_visible_empty_password_alert(self):
        self.password_alert.check_visible()
        self.password_alert.check_have_text("Password is a required field")

    def check_visible_error_email_incorrect_notification(self):
        self.toast_notification.check_visible("error", "Password matched but email is incorrect.")

    def check_visible_error_password_incorrect_notification(self):
        self.toast_notification.check_visible("error", "Username matched but password is incorrect.")

    def check_visible_error_credentials_incorrect_notification(self):
        self.toast_notification.check_visible("error", "Neither email nor password matched.")
