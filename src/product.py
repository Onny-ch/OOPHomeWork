from typing import Any


class Product:
    name: str
    description: str
    __price: float
    quantity: int
    list_of_products = []

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        Product.list_of_products.append(self)

    @classmethod
    def new_product(cls, new_product: dict[str: Any]):
        """Класс-метод для создания нового обьекта класса Product"""
        for item in cls.list_of_products:
            if new_product["name"] == item.name:
                item.quantity += new_product["quantity"]
                if item.__price < new_product["price"]:
                    item.__price = new_product["price"]
                return item
        return cls(**new_product)

    @property
    def price(self):
        """Геттер цены"""
        return self.__price

    @price.setter
    def price(self, new_price):
        """Сеттер цены с дополнительными проверками"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            if new_price < self.__price:
                yon = input("Вы уверены, что хотите снизить цену? (y/n) ")
                if yon.lower() == "y":
                    self.__price = new_price
                    print("Цена изменена на:", new_price)
            else:
                self.__price = new_price
