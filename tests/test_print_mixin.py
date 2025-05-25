from src.product import Product


def test_print_mixin(capsys):
    Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    message = capsys.readouterr()
    assert message.out.strip().split("\n")[0] == "Product(Iphone 15, 512GB, Gray space, 210000.0, 8)"
