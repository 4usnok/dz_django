from catalog.models import Product
from config.settings import CACHE_ENABLED


def products_by_category(category_id):
    products = Product.objects.filter(category_id=category_id)
    if CACHE_ENABLED:
        return products
