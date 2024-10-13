from src.category import Category


class ProductEnumeration:
    def __init__(self, category_object: Category):
        self.object = category_object
        self.a = 0

    def __iter__(self) -> "ProductEnumeration":
        return self

    def __next__(self) -> str:
        products = self.object.products.split("\n")
        products.remove("")
        if self.a < len(products):
            product = products[self.a]
            self.a += 1
            return product
        else:
            raise StopIteration
