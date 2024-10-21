from src.base_order import BaseOrder


class Order(BaseOrder):
    product: str
    description: str
    price: float
    quantity: int
    # max_limit_order: bool = True
    # current_order_count: bool = False

    def __init__(self, product: str, description: str, price: float, quantity: int) -> None:
        self.product = product
        self.description = description
        self.price = price
        self.quantity = quantity
        super().__init__()
        # self.current_order_count = True

    def __str__(self) -> str:
        return f"Товар: {self.product}, количество: {self.quantity}, цена: {self.price}"
