from src.product import Product


class Category:
    name: str
    description: str
    __products: list[Product]
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list[Product]):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(self.__products)

    def __str__(self):
        counter = 0
        for prod in self.__products:
            counter += prod.quantity

        return f"{self.name}, количество продуктов: {counter} шт."

    def add_product(self, new_product: Product) -> None:
        """Метод добавления нового продукта"""
        self.__products.append(new_product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """Геттер получения продуктов построчно"""
        products_str = ""
        for product in self.__products:
            products_str += str(product) + '\n'
        return products_str
