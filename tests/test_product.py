from unittest.mock import patch

import pytest

from src.product import Product


def test_product_init(product1, product2, product3):
    assert product1.name == "Samsung Galaxy S23 Ultra"
    assert product1.description == "256GB, Серый цвет, 200MP камера"
    assert product1.price == 180000.0
    assert product1.quantity == 5

    assert product2.name == "Iphone 15"
    assert product2.description == "512GB, Gray space"
    assert product2.price == 210000.0
    assert product2.quantity == 8

    assert product3.name == "Xiaomi Redmi Note 11"
    assert product3.description == "1024GB, Синий"
    assert product3.price == 31000.0
    assert product3.quantity == 14


def test_new_product(product1, product2, product1_dict, product2_dict):
    new_product1 = Product.new_product(product1_dict)
    assert new_product1.quantity == 10
    assert new_product1.price == 200000.0

    new_product2 = Product.new_product(product2_dict)
    assert new_product2.name == "Iphone 17"
    assert new_product2.description == "1024Tb, Gray space"
    assert new_product2.price == 1600000.0
    assert new_product2.quantity == 1


def test_product_private_price(capsys, product1):
    product1.price = 0
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"

    product1.price = 190000
    assert product1.price == 190000

    with patch("builtins.input", side_effect=["n"]):
        product1.price = 160000
        assert product1.price == 190000

    with patch("builtins.input", side_effect=["y"]):
        product1.price = 160000
        assert product1.price == 160000


def test_product_add(capsys, product1, product2):
    print(product1 + product2)
    message = capsys.readouterr()
    assert message.out.strip() == "2580000.0"


def test_product_add_error(second_smartphone, second_lawn_grass):
    with pytest.raises(TypeError):
        res = second_smartphone + second_lawn_grass


def test_smartphone_init(first_smartphone):
    assert first_smartphone.name == "Samsung Galaxy S23 Ultra"
    assert first_smartphone.description == "256GB, Серый цвет, 200MP камера"
    assert first_smartphone.price == 180000.0
    assert first_smartphone.quantity == 5
    assert first_smartphone.efficiency == 95.5
    assert first_smartphone.model == "S23 Ultra"
    assert first_smartphone.memory == 256
    assert first_smartphone.color == "Серый"


def test_lawn_grass_init(first_lawn_grass):
    assert first_lawn_grass.name == "Газонная трава"
    assert first_lawn_grass.description == "Элитная трава для газона"
    assert first_lawn_grass.price == 500.0
    assert first_lawn_grass.quantity == 20
    assert first_lawn_grass.country == "Россия"
    assert first_lawn_grass.germination_period == "7 дней"
    assert first_lawn_grass.color == "Зеленый"
