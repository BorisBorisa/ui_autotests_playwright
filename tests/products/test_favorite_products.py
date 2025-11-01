import pytest
import allure

from pages.product.product_page import ProductPage
from pages.products.products_page import ProductsPage
from pages.favorites.favorites_page import FavoritesPage

from tools.routes import AppRoute

from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from allure_commons.types import Severity

@allure.epic(AllureEpic.PRODUCT_CATALOG)
@allure.feature(AllureFeature.FAVORITES)

@pytest.mark.regression
@pytest.mark.products
@pytest.mark.favorite
class TestFavoriteProducts:
    @allure.title("Add products to favorites")
    @allure.story(AllureStory.ADDS_PRODUCT_TO_FAVORITES)
    def test_add_products_to_favorites(
            self,
            products_page_with_state: ProductsPage,
            favorites_page: FavoritesPage
    ):
        added_products = []
        products_page = products_page_with_state

        products_page.visit(AppRoute.PRODUCTS)

        products_page.product_card.click_favorite_button(0)
        added_products.append(products_page.product_card.get_product(0))
        products_page.product_card.check_favorite_button_is_active(0)
        products_page.toast_notification.check_visible_added_to_favorites_notification()

        products_page.product_card.click_favorite_button(5)
        added_products.append(products_page.product_card.get_product(5))
        products_page.product_card.check_favorite_button_is_active(5)
        products_page.toast_notification.check_visible_added_to_favorites_notification()

        products_page.reload()

        products_page.product_card.check_favorite_button_is_active(0)
        products_page.product_card.check_favorite_button_is_active(5)

        products_page.header.click_user_favorites()
        favorites_page.is_page_opened()

        favorites_page.check_favorites_products_equals_expected(added_products)

    @allure.title("Add products to favorites from products card")
    @allure.story(AllureStory.ADDS_PRODUCT_TO_FAVORITES)
    def test_add_product_to_favorites_from_product_card(
            self,
            products_page_with_state: ProductsPage,
            product_page: ProductPage,
            favorites_page: FavoritesPage
    ):
        products_page_with_state.visit(AppRoute.PRODUCTS)

        products_page_with_state.product_card.click(2)
        product_page.is_page_opened()

        product_page.click_favorite_button()
        product = product_page.get_product()
        product_page.check_favorite_button_is_active()
        product_page.toast_notification.check_visible_added_to_favorites_notification()

        product_page.reload()

        product_page.check_favorite_button_is_active()

        product_page.header.click_user_favorites()
        favorites_page.is_page_opened()

        favorites_page.check_favorites_products_equals_expected([product])

    @allure.title("Removing products from favorites")
    @allure.story(AllureStory.REMOVES_PRODUCT_FROM_FAVORITES)
    def test_removing_product_from_favorites(
            self,
            products_page_with_state: ProductsPage,
            product_page: ProductPage,
            favorites_page: FavoritesPage
    ):
        products_page = products_page_with_state
        products_page.visit(AppRoute.PRODUCTS)

        products_page.product_card.click_favorite_button(0)
        products_page.product_card.click_favorite_button(1)
        products_page.product_card.click_favorite_button(2)

        products_page.product_card.click_favorite_button(0)
        products_page.product_card.check_favorite_button_is_inactive(0)
        products_page.toast_notification.check_visible_remove_from_favorites_notification()

        products_page.product_card.click(1)
        product_page.is_page_opened()

        product_page.click_favorite_button()
        product_page.check_favorite_button_is_inactive()
        product_page.toast_notification.check_visible_remove_from_favorites_notification()

        product_page.click_back_to_products_button()

        products_page.product_card.check_favorite_button_is_inactive(1)

        products_page.header.click_user_favorites()
        favorites_page.is_page_opened()

        favorites_page.product_card.click_favorite_button(0)
        favorites_page.toast_notification.check_visible_remove_from_favorites_notification()

        favorites_page.empty_view.check_visible()
        favorites_page.empty_view.click_continue_shopping_link()

        products_page.is_page_opened()
