from enum import Enum


class AllureEpic(str, Enum):
    USER_ACCOUNT = "user account"
    PRODUCT_CATALOG = "product catalog"
    SHOPPING_CART_CHECKOUT = "shopping cart & checkout"
