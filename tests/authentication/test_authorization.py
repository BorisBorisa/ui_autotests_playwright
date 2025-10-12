from pages.authentication.login_page import LoginPage
from pages.products.products_page import ProductsPage

from tools.routes import AppRoute
from config import settings


class TestAuthorization:
    def test_successful_authorization(
            self,
            login_page: LoginPage,
            products_page: ProductsPage
    ):
        login_page.visit(url=AppRoute.LOGIN)

        login_page.fill_login_form(
            email=settings.test_user.email,
            password=settings.test_user.password
        )

        login_page.click_login_button()

        products_page.header.check_visible(email=settings.test_user.email)
        products_page.title.check_visible()
        products_page.products_order_menu.check_visible()

    def test_wrong_email_authorization(self):
        pass

    def test_wrong_password_authorization(self):
        pass

    def test_wrong_credentials_authorization(self):
        pass

    def test_navigate_from_authorization_to_home(self):
        pass
