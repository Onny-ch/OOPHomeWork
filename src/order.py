from src.base_order import BaseOrder


class Order(BaseOrder):
    product: str
    description: str
    price: float
    quantity: int
    # max_limit_order: bool = True
    # current_order_count: bool = False

    def __init__(self, product, description, quantity, price):
        self.product = product
        self.description = description
        self.quantity = quantity
        self.price = price
        # self.current_order_count = True

    def __str__(self):
        return f"Товар: {self.product}, количество: {self.quantity}, цена: {self.price}"
