from src.category import Category


def test_counts(first_category, product1, product2, product3):
    assert Category.category_count == 1
    assert Category.product_count == 3


def test_category_init(first_category, product1, product2, product3):
    assert first_category.name == "Смартфоны"
    assert (
        first_category.description == "Смартфоны, как средство не только коммуникации, "
        "но и получения дополнительных функций для удобства жизни"
    )
    assert first_category.products == [product1, product2, product3]
