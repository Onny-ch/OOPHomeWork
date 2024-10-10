import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def product1():
    return Product(
        name="Samsung Galaxy S23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5,
    )


@pytest.fixture
def product1_str():
    return "Samsung Galaxy S23 Ultra, 180000.0 Остаток: 5\n"


@pytest.fixture
def product1_dict():
    return {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 200000.0,
        "quantity": 5
    }


@pytest.fixture
def product2():
    return Product(name="Iphone 15", description="512GB, Gray space", price=210000.0, quantity=8)


@pytest.fixture
def product2_dict():
    return {
        "name": "Iphone 17",
        "description": "1024Tb, Gray space",
        "price": 1600000.0,
        "quantity": 1
    }


@pytest.fixture
def product2_str():
    return "Iphone 15, 210000.0 Остаток: 8\n"


@pytest.fixture
def product3():
    return Product(
        name="Xiaomi Redmi Note 11",
        description="1024GB, Синий",
        price=31000.0,
        quantity=14,
    )


@pytest.fixture
def product3_str():
    return "Xiaomi Redmi Note 11, 31000.0 Остаток: 14\n"


@pytest.fixture
def product4():
    return Product(
        name="55\" QLED 4K",
        description="Фоновая подсветка",
        price=123000.0,
        quantity=7
    )


@pytest.fixture
def first_category(product1, product2, product3):
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации, "
        "но и получения дополнительных функций для удобства жизни",
        products=[product1, product2, product3],
    )
