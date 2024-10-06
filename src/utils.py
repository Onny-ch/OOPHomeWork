import json
import os
from typing import Any

from src.category import Category
from src.product import Product


def read_file(path: str) -> Any:
    """Функция для чтения json файла"""
    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="UTF-8") as file:
        data = json.load(file)
    return data


def create_objects_with_json(data: list[dict[Any, Any]]) -> list[Category]:
    """Функция создающая элементы категорий и продуктов из данных"""
    category_list = []
    for item in data:
        products_list = []
        for prod in item["products"]:
            products_list.append(Product(**prod))
        item["products"] = products_list
        category_list.append(Category(**item))
    return category_list
