from dataclasses import dataclass


@dataclass(frozen=True, order=True)
class Product:
    name: str
    description: str
    img_src: str
    price: str
