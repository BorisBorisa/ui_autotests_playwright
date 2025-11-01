from enum import Enum


class AllureFeature(str, Enum):
    AUTHENTICATION = "Authentication"

    CARD_MANAGEMENT = "Cart management"
    CHECKOUT = "Checkout process"

    FAVORITES = "Favorites"
    PRODUCTS_SORTING = "Products sorting"

