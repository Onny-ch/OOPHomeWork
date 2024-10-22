from src.base_order import BaseOrder


class Order(BaseOrder):
    product: str
    description: str
    price: float
    quantity: int
    current_order = None

    def __init__(self, product: str, description: str, price: float, quantity: int) -> None:
        self.product = product
        self.description = description
        self.price = price
        self.quantity = quantity
        super().__init__()

    def __new__(cls, *args, **kwargs):
        if cls.current_order is None:
            cls.current_order = super().__new__(cls)
        return cls.current_order

    def __str__(self) -> str:
        return (
            f"Товар: {self.product}, "
            f"информация о товаре: {self.description}, "
            f"количество: {self.quantity}, "
            f"цена: {self.price}"
        )
