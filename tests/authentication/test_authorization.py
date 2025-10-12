from pages.authentication.login_page import LoginPage
from pages.products.products_page import ProductsPage

from tools.routes import AppRoute
from config import settings


class TestAuthorization:
    def test_successful_authorization(self, login_page: LoginPage, products_page: ProductsPage):
        login_page.visit(url=AppRoute.LOGIN)

        login_page.fill_login_form(
            email=settings.test_user.email,
            password=settings.test_user.password
        )

        login_page.click_login_button()

        products_page.header.check_visible(email=settings.test_user.email)
        products_page.title.check_visible()
        products_page.products_order_menu.check_visible()

    def test_wrong_email_authorization(self, login_page: LoginPage):
        login_page.visit(url=AppRoute.LOGIN)

        login_page.fill_login_form(
            email=settings.test_data.invalid_email,
            password=settings.test_user.password
        )

        login_page.click_login_button()

        login_page.check_visible_wrong_email_alert()
        login_page.check_visible_error_email_incorrect_notification()

        login_page.fill_login_form(
            email="",
            password=settings.test_user.password
        )

        login_page.click_login_button()

        login_page.check_visible_empty_email_alert()

    def test_wrong_password_authorization(self, login_page: LoginPage):
        login_page.visit(url=AppRoute.LOGIN)

        login_page.fill_login_form(
            email=settings.test_user.email,
            password=settings.test_data.invalid_password
        )

        login_page.click_login_button()

        login_page.check_visible_wrong_password_alert()
        login_page.check_visible_error_password_incorrect_notification()

        login_page.fill_login_form(
            email=settings.test_user.email,
            password=""
        )

        login_page.check_visible_empty_password_alert()

    def test_navigate_from_authorization_to_home(self):
        pass
    def test_wrong_credentials_authorization(self, login_page: LoginPage):
        login_page.visit(url=AppRoute.LOGIN)

        login_page.fill_login_form(
            email=settings.test_data.invalid_email,
            password=settings.test_data.invalid_password
        )

        login_page.click_login_button()

        login_page.check_visible_wrong_email_alert()
        login_page.check_visible_wrong_password_alert()
        login_page.check_visible_error_credentials_incorrect_notification()

        login_page.fill_login_form(
            email="",
            password=""
        )

        login_page.check_visible_empty_email_alert()
        login_page.check_visible_empty_password_alert()
