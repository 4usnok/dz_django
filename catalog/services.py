from catalog.models import Product

def products_by_category(category_id):
    products = Product.objects.filter(category_id=category_id)
    return products
