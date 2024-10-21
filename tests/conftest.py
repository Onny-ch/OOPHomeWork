import pytest

from src.category import Category
from src.product import LawnGrass, Product, Smartphone


@pytest.fixture
def product1():
    return Product(
        name="Samsung Galaxy S23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5,
    )


@pytest.fixture
def product1_str(product1):
    return f"{str(product1)}\n"


@pytest.fixture
def product1_dict():
    return {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 200000.0,
        "quantity": 5,
    }


@pytest.fixture
def product2():
    return Product(name="Iphone 15", description="512GB, Gray space", price=210000.0, quantity=8)


@pytest.fixture
def product2_str(product2):
    return f"{str(product2)}\n"


@pytest.fixture
def product2_dict():
    return {"name": "Iphone 17", "description": "1024Tb, Gray space", "price": 1600000.0, "quantity": 1}


@pytest.fixture
def product3():
    return Product(
        name="Xiaomi Redmi Note 11",
        description="1024GB, Синий",
        price=31000.0,
        quantity=14,
    )


@pytest.fixture
def product3_str(product3):
    return f"{str(product3)}\n"


@pytest.fixture
def product4():
    return Product(name='55" QLED 4K', description="Фоновая подсветка", price=123000.0, quantity=7)


@pytest.fixture
def first_category(product1, product2, product3):
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации, "
        "но и получения дополнительных функций для удобства жизни",
        products=[product1, product2, product3],
    )


@pytest.fixture
def list_with_category_string():
    return [
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.",
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.",
        "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.",
    ]


@pytest.fixture
def first_smartphone():
    return Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )


@pytest.fixture
def second_smartphone():
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")


@pytest.fixture
def first_lawn_grass():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture
def non_product():
    return "I'm a STRING"


@pytest.fixture
def second_lawn_grass():
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")


@pytest.fixture
def category_smartphones(first_smartphone, second_smartphone):
    return Category("Смартфоны", "Высокотехнологичные смартфоны", [first_smartphone, second_smartphone])


@pytest.fixture
def category_grass(first_lawn_grass, second_lawn_grass):
    return Category("Газонная трава", "Различные виды газонной травы", [first_lawn_grass, second_lawn_grass])
