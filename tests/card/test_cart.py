import pytest
import allure

from pages.product.product_page import ProductPage
from pages.products.products_page import ProductsPage
from pages.favorites.favorites_page import FavoritesPage
from pages.cart.cart_page import CardPage

from tools.routes import AppRoute


@pytest.mark.regression
@pytest.mark.products
@pytest.mark.card
class TestCart:
    @allure.title("Add products to cart")
    def test_add_products_to_cart(
            self,
            products_page_with_state: ProductsPage,
            card_page: CardPage
    ):
        added_products = []
        products_page = products_page_with_state

        products_page.visit(AppRoute.PRODUCTS)

        products_page.product_card.click_add_to_card_button(0)
        added_products.append(products_page.product_card.get_product(0))
        products_page.product_card.check_add_to_cart_button_in_remove_state(0)
        products_page.toast_notification.check_visible_added_to_cart_notification()

        products_page.product_card.click_add_to_card_button(2)
        added_products.append(products_page.product_card.get_product(2))
        products_page.product_card.check_add_to_cart_button_in_remove_state(2)
        products_page.toast_notification.check_visible_added_to_cart_notification()

        products_page.header.check_cart_counter_value(2)

        products_page.reload()

        products_page.product_card.check_add_to_cart_button_in_remove_state(0)
        products_page.product_card.check_add_to_cart_button_in_remove_state(2)

        products_page.product_card.click_cart_button()
        card_page.is_page_opened()

        card_page.check_cart_products_equals_expected(added_products)

    @allure.title("Add products to cart from products card")
    def test_add_product_to_cart_from_product_card(
            self,
            products_page_with_state: ProductsPage,
            product_page: ProductPage,
            card_page: CardPage
    ):
        products_page_with_state.visit(AppRoute.PRODUCTS)

        products_page_with_state.product_card.click(8)
        product_page.is_page_opened()

        product_page.click_add_to_card_button()
        product = product_page.get_product()
        product_page.toast_notification.check_visible_added_to_cart_notification()

        product_page.header.check_cart_counter_value(1)

        product_page.header.click_cart_button()
        card_page.is_page_opened()

        card_page.check_cart_products_equals_expected([product])

    @allure.title("Add products to cart from favorites")
    def test_add_product_to_cart_from_favorites_page(
            self,
            products_page_with_state: ProductsPage,
            favorites_page: FavoritesPage,
            card_page: CardPage
    ):
        products_page_with_state.visit(AppRoute.PRODUCTS)

        products_page_with_state.product_card.click_favorite_button(5)

        products_page_with_state.header.click_user_favorites()
        favorites_page.is_page_opened()

        favorites_page.product_card.click_add_to_card_button(0)
        product = favorites_page.product_card.get_product(0)
        favorites_page.toast_notification.check_visible_added_to_cart_notification()
        favorites_page.product_card.check_add_to_cart_button_in_remove_state(0)

        favorites_page.header.check_cart_counter_value(1)

        favorites_page.header.click_cart_button()
        card_page.is_page_opened()

        card_page.check_cart_products_equals_expected([product])
