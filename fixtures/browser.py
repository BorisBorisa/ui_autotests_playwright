import pytest
from _pytest.fixtures import SubRequest

from typing import Generator

from playwright.sync_api import Playwright, Page

from pages.authentication.login_page import LoginPage
from pages.products.products_page import ProductsPage

from tools.routes import AppRoute
from tools.playwright.pages import initialize_playwright_page

from config import settings


@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright):
    browser = playwright.chromium.launch(headless=settings.headless)
    context = browser.new_context(base_url=settings.get_base_url)
    page = context.new_page()

    login_page = LoginPage(page)
    products_page = ProductsPage(page)
    login_page.visit(AppRoute.LOGIN)

    login_page.fill_login_form(
        email=settings.test_user.email,
        password=settings.test_user.password
    )

    login_page.click_login_button()
    products_page.is_page_opened()

    context.storage_state(path=settings.browser_state_file)
    browser.close()


@pytest.fixture(params=settings.browsers)
def page_with_state(
        initialize_browser_state,
        request: SubRequest,
        playwright: Playwright
) -> Generator[Page, None, None]:
    yield from initialize_playwright_page(
        playwright,
        test_name=request.node.name,
        browser_type=request.param,
        storage_state=settings.browser_state_file
    )


@pytest.fixture(params=settings.browsers)
def page(
        request: SubRequest,
        playwright: Playwright
) -> Generator[Page, None, None]:
    yield from initialize_playwright_page(
        playwright,
        test_name=request.node.name,
        browser_type=request.param
    )
