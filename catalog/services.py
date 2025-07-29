from django.core.cache import cache

from catalog.models import Product
from config.settings import CACHE_ENABLED


def products_by_category(category_id):
    if CACHE_ENABLED:
        return Product.objects.filter(category_id=category_id)
    key = f"products_cat_{category_id}"
    products = cache.get(key)
    if products is None:
        products = list(Product.objects.filter(category_id=category_id))
        cache.set(key, products)
    return products
