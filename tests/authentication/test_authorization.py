import pytest
import allure

from pages.authentication.login_page import LoginPage
from pages.products.products_page import ProductsPage

from tools.routes import AppRoute

from config import settings


@pytest.mark.regression
@pytest.mark.authorization
class TestAuthorization:
    @allure.title("User login with correct email and password")
    def test_successful_authorization(self, login_page: LoginPage, products_page: ProductsPage):
        login_page.visit(url=AppRoute.LOGIN)

        login_page.fill_login_form(
            email=settings.test_user.email,
            password=settings.test_user.password
        )

        login_page.click_login_button()
        products_page.is_page_opened()

    @allure.title("User logout")
    def test_user_logout(self, products_page_with_state: ProductsPage, login_page_with_state: LoginPage):
        products_page_with_state.visit(url=AppRoute.PRODUCTS)

        products_page_with_state.header.click_user_log_out()
        products_page_with_state.logout_dialog.check_visible()

        products_page_with_state.logout_dialog.click_logout_button()

        login_page_with_state.is_page_opened()

    @allure.title("User login with wrong email")
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

    @allure.title("User login with wrong password")
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

    @allure.title("User login with wrong credentials")
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

    @allure.title("Navigation from login page to home page")
    def test_navigate_from_authorization_to_home(self, login_page: LoginPage):
        login_page.visit(url=AppRoute.LOGIN)

        login_page.click_back_to_home_link()

        login_page.check_current_url(settings.get_base_url)
