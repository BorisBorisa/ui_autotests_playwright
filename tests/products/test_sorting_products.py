import pytest
import allure

from pages.products.products_page import ProductsPage
from tools.routes import AppRoute

from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from allure_commons.types import Severity

@allure.epic(AllureEpic.PRODUCT_CATALOG)
@allure.feature(AllureFeature.PRODUCTS_SORTING)

@pytest.mark.regression
@pytest.mark.products
@pytest.mark.sorting
class TestSortingProducts:
    @allure.title("Sorting products by price low to high")
    @allure.story(AllureStory.SORTS_PRODUCTS_BY_PRICE)
    @allure.severity(Severity.NORMAL)
    def test_verify_sorting_by_price_low_to_high(self, products_page_with_state: ProductsPage):
        products_page_with_state.visit(AppRoute.PRODUCTS)

        products_page_with_state.products_order_menu.click_low_to_high_order()
        products_page_with_state.check_prices_sorted_low_to_high()

    @allure.title("Sorting products by price high to low")
    @allure.story(AllureStory.SORTS_PRODUCTS_BY_PRICE)
    @allure.severity(Severity.NORMAL)
    def test_verify_sorting_by_price_high_to_low(self, products_page_with_state: ProductsPage):
        products_page_with_state.visit(AppRoute.PRODUCTS)

        products_page_with_state.products_order_menu.click_high_to_low_order()
        products_page_with_state.check_prices_sorted_high_to_low()

    @allure.title("Sorting products by name alphabetically a to z")
    @allure.story(AllureStory.SORTS_PRODUCTS_BY_NAME)
    @allure.severity(Severity.MINOR)
    def test_verify_sorting_by_name_a_to_z(self, products_page_with_state: ProductsPage):
        products_page_with_state.visit(AppRoute.PRODUCTS)

        products_page_with_state.products_order_menu.click_ascending_order()
        products_page_with_state.check_names_sorted_a_to_z()

    @allure.title("Sorting products by name alphabetically z to a")
    @allure.story(AllureStory.SORTS_PRODUCTS_BY_NAME)
    @allure.severity(Severity.MINOR)
    def test_verify_sorting_by_name_z_to_a(self, products_page_with_state: ProductsPage):
        products_page_with_state.visit(AppRoute.PRODUCTS)

        products_page_with_state.products_order_menu.click_descending_order()
        products_page_with_state.check_names_sorted_z_to_a()
