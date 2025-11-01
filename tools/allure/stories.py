from enum import Enum


class AllureStory(str, Enum):
    LOGIN = "User login"

    ADDS_PRODUCT_TO_CARD = "Adds product to cart"
    REMOVES_PRODUCT_FROM_CARD = "Removes product from cart"

    CHECKOUT_MULTIPLY_PRODUCTS = "Checkout with multiple products"

    ADDS_PRODUCT_TO_FAVORITES = "Adds product to wishlist"
    REMOVES_PRODUCT_FROM_FAVORITES = "removes product from wishlist"

    SORTS_PRODUCTS_BY_PRICE = "sorts products by price"
    SORTS_PRODUCTS_BY_NAME = "sorts products by name"




