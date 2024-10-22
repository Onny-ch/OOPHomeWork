from typing import Any

from src.base_product import BaseProduct
from src.print_mixin import PrintMixin


class Product(BaseProduct, PrintMixin):
    name: str
    description: str
    price: float
    quantity: int
    list_of_products: list[Any] = []

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        super().__init__(name, description, price, quantity)
        Product.list_of_products.append(self)

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> float:
        if other.__class__ is self.__class__:  # isinstance(other, self.__class__)
            add = self.quantity * self.price + other.quantity * other.price
            return add
        else:
            raise TypeError

    @classmethod
    def new_product(cls, new_product_dict: dict[str, Any]) -> Any:
        """Класс-метод для создания нового обьекта класса Product"""
        for item in cls.list_of_products:
            if new_product_dict["name"] == item.name:
                item.quantity += new_product_dict["quantity"]
                if item.price < new_product_dict["price"]:
                    item.price = new_product_dict["price"]
                return item
        return cls(**new_product_dict)


class Smartphone(Product):
    efficiency: float
    model: str
    memory: int
    color: str

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    country: str
    germination_period: str
    color: str

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
