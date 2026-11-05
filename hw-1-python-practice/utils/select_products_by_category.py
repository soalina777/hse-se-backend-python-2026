from models.product import Product


def select_products_by_category(
    products: list[Product], category: str
) -> list[Product]:
    result = []

    for product in products:
        if product.category == category:
            result.append(product)

    return result