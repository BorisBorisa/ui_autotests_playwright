from enum import Enum


class AppRoute(str, Enum):
    LOGIN = "./ecommerce/login"
    PRODUCTS = "./ecommerce"
    FAVORITES = "./ecommerce/favorites"
    CART = "./ecommerce/cart"
