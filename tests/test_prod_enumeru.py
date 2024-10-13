import pytest

from src.prod_enumeru import ProductEnumeration


def test_iteration_category_products(capsys, first_category):
    category = ProductEnumeration(first_category)
    assert next(category) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."
    assert next(category) == "Iphone 15, 210000.0 руб. Остаток: 8 шт."
    assert next(category) == "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт."
    with pytest.raises(StopIteration):
        next(category)

    for item in category:
        print(item)
        assert capsys.readouterr().out.strip() is None
