import pytest
from playwright.sync_api import Page

from pages.authentication.login_page import LoginPage
from pages.cart.cart_page import CardPage
from pages.favorites.favorites_page import FavoritesPage
from pages.products.products_page import ProductsPage
from pages.product.product_page import ProductPage

from pages.checkout.checkout_complete_page import CheckoutCompletePage
from pages.checkout.checkout_information_page import CheckoutInformationPage
from pages.checkout.checkout_overview_page import CheckoutOverviewPage


@pytest.fixture
def login_page(page: Page) -> LoginPage:
    return LoginPage(page)


@pytest.fixture
def card_page(page_with_state: Page) -> CardPage:
    return CardPage(page_with_state)


@pytest.fixture
def favorites_page(page_with_state: Page) -> FavoritesPage:
    return FavoritesPage(page_with_state)


@pytest.fixture
def products_page(page: Page) -> ProductsPage:
    return ProductsPage(page)


@pytest.fixture
def products_page_with_state(page_with_state: Page) -> ProductsPage:
    return ProductsPage(page_with_state)


@pytest.fixture
def product_page(page_with_state: Page) -> ProductPage:
    return ProductPage(page_with_state)


@pytest.fixture
def checkout_complete_page(page_with_state: Page) -> CheckoutCompletePage:
    return CheckoutCompletePage(page_with_state)


@pytest.fixture
def checkout_information_page(page_with_state: Page) -> CheckoutInformationPage:
    return CheckoutInformationPage(page_with_state)


@pytest.fixture
def checkout_overview_page(page_with_state: Page) -> CheckoutOverviewPage:
    return CheckoutOverviewPage(page_with_state)
