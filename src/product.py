from typing import Any


class Product:
    name: str
    description: str
    __price: float
    quantity: int
    list_of_products: list[Any] = []

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        Product.list_of_products.append(self)

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> float:
        add = self.quantity * self.__price + other.quantity * other.price
        return add

    @classmethod
    def new_product(cls, new_product_dict: dict[str, Any]) -> Any:
        """Класс-метод для создания нового обьекта класса Product"""
        for item in cls.list_of_products:
            if new_product_dict["name"] == item.name:
                item.quantity += new_product_dict["quantity"]
                if item.__price < new_product_dict["price"]:
                    item.__price = new_product_dict["price"]
                return item
        return cls(**new_product_dict)

    @property
    def price(self) -> float:
        """Геттер цены"""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """Сеттер цены с дополнительными проверками"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            if new_price < self.__price:
                yon = input("Вы уверены, что хотите снизить цену? (y/n) ")
                if yon.lower() == "y":
                    self.__price = new_price
            else:
                self.__price = new_price
