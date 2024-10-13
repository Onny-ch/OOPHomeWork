import pytest

from src.prod_enumeru import ProductEnumeration


def test_iteration_category_products(first_category, list_with_category_string):
    category = ProductEnumeration(first_category)
    for item in category:
        assert item == list_with_category_string[0]
        assert next(category) == list_with_category_string[1]
        assert next(category) == list_with_category_string[2]
        with pytest.raises(StopIteration):
            next(category)
