from django.core.cache import cache
from django.conf import settings
from .models import Product

def get_products_by_category(category_id):
    if settings.CACHE_ENABLED:
        key = f'products_list_{category_id}'
        products = cache.get(key)
        if products is None:
            products = Product.objects.filter(category_id=category_id)
            cache.set(key, products)
    else:
        products = Product.objects.filter(category_id=category_id)
    return products