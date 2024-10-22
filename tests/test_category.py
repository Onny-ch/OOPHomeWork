import pytest

from src.category import Category


def test_counts(first_category):
    assert Category.category_count == 1
    assert Category.product_count == 3


def test_category_init(first_category, product1_str, product2_str, product3_str):
    assert first_category.name == "Смартфоны"
    assert (
        first_category.description == "Смартфоны, как средство не только коммуникации, "
        "но и получения дополнительных функций для удобства жизни"
    )
    assert first_category.products == f"{product1_str}{product2_str}{product3_str}"


def test_category_add_product(first_category, product4):
    first_category.add_product(product4)
    assert first_category.product_count == 10


def test_category_str(capsys, first_category):
    assert str(first_category) == "Смартфоны, количество продуктов: 27 шт."

    print(first_category)
    assert capsys.readouterr().out.strip().split("\n")[-1] == "Смартфоны, количество продуктов: 27 шт."


def test_category_add_product_error(category_smartphones, category_grass, non_product):
    with pytest.raises(TypeError):
        category_smartphones.add_product(non_product)
    with pytest.raises(TypeError):
        category_grass.add_product(non_product)
