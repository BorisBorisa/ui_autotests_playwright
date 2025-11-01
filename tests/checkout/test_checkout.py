import pytest
import allure

from pages.products.products_page import ProductsPage
from pages.cart.cart_page import CardPage
from pages.checkout.checkout_information_page import CheckoutInformationPage
from pages.checkout.checkout_overview_page import CheckoutOverviewPage
from pages.checkout.checkout_complete_page import CheckoutCompletePage

from tools.routes import AppRoute
from config import settings

from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from allure_commons.types import Severity

@allure.epic(AllureEpic.SHOPPING_CART_CHECKOUT)
@allure.feature(AllureFeature.CHECKOUT)
@allure.story(AllureStory.CHECKOUT_MULTIPLY_PRODUCTS)

@pytest.mark.regression
@pytest.mark.checkout
class TestCheckout:
    @allure.title("Checkout with multiple products")
    @allure.severity(Severity.BLOCKER)
    def test_checkout_with_multiple_products(
            self,
            products_page_with_state: ProductsPage,
            card_page: CardPage,
            checkout_information_page: CheckoutInformationPage,
            checkout_overview_page: CheckoutOverviewPage,
            checkout_complete_page: CheckoutCompletePage
    ):
        added_products = []
        products_page = products_page_with_state

        products_page.visit(AppRoute.PRODUCTS)

        products_page.product_card.click_add_to_card_button(0)
        added_products.append(products_page.product_card.get_product(0))

        products_page.product_card.click_add_to_card_button(7)
        added_products.append(products_page.product_card.get_product(7))

        products_page.header.click_cart_button()
        card_page.is_page_opened()

        card_page.card_item.check_cart_items_equal_expected(added_products)

        card_page.click_checkout_button()
        checkout_information_page.is_page_opened()

        checkout_information_page.fill_checkout_information_form(
            first_name=settings.test_user.first_name,
            last_name=settings.test_user.last_name,
            zip_code=settings.test_user.zip_code
        )
        checkout_information_page.check_visible_checkout_information_form(
            email=settings.test_user.email,
            first_name=settings.test_user.first_name,
            last_name=settings.test_user.last_name,
            zip_code=settings.test_user.zip_code
        )

        checkout_information_page.click_continue_button()
        checkout_overview_page.is_page_opened()

        checkout_overview_page.card_item.check_cart_items_equal_expected(added_products)
        checkout_overview_page.check_visible_checkout_summary()

        checkout_overview_page.click_finish_button()
        checkout_complete_page.is_page_opened()

        checkout_complete_page.check_visible_complete_message()
        checkout_complete_page.click_continue_shopping_button()

        products_page.is_page_opened()
