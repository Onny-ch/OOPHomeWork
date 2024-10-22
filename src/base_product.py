from abc import ABC, abstractmethod


class BaseProduct(ABC):
    name: str
    description: str
    __price: float
    quantity: int

    @abstractmethod
    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()

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
