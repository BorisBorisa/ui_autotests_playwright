import pytest
import allure

from pages.products.products_page import ProductsPage
from pages.favorites.favorites_page import FavoritesPage

from tools.routes import AppRoute

from tools.logger import get_logger

logger = get_logger("TEST_TEST")


@pytest.mark.regression
@pytest.mark.products
@pytest.mark.favorite
class TestFavoriteProducts:
    def test_add_product_to_favorites(self, products_page_with_state: ProductsPage, favorites_page: FavoritesPage):
        added_products = []
        products_page = products_page_with_state

        products_page.visit(AppRoute.PRODUCTS)

        products_page.click_product_favorite_button(0)
        added_products.append(products_page.product_card.get_product(0))
        products_page.check_product_favorite_button_is_active(0)
        products_page.check_visible_added_to_favorites_notification()

        products_page.click_product_favorite_button(5)
        added_products.append(products_page.product_card.get_product(5))
        products_page.check_product_favorite_button_is_active(5)
        products_page.check_visible_added_to_favorites_notification()

        products_page.reload()

        products_page.check_product_favorite_button_is_active(0)

        products_page.header.user_profile_menu.click_user_favorites()
        favorites_page.is_page_opened()

        favorites_page.check_favorites_products_equals_expected(added_products)

    def test_removing_product_from_favorites(
            self,
            products_page_with_state: ProductsPage,
            favorites_page: FavoritesPage
    ):
        products_page = products_page_with_state
        products_page.visit(AppRoute.PRODUCTS)

        products_page.click_product_favorite_button(0)
        products_page.click_product_favorite_button(2)

        products_page.click_product_favorite_button(0)
        products_page.check_product_favorite_button_is_inactive(0)

        products_page.check_visible_remove_from_favorites_notification()

        products_page.header.user_profile_menu.click_user_favorites()
        favorites_page.is_page_opened()

        favorites_page.click_product_favorite_by_index(0)
        favorites_page.check_visible_remove_from_favorites_notification()

        favorites_page.empty_view.check_visible()
        favorites_page.empty_view.click_continue_shopping_link()

        products_page.is_page_opened()
