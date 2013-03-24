from django.conf import settings

# Allows the usage of a custom url set in your project's settings.py, 
# Will default to lcboapi.com/products if the setting does not exist.
LCBO_PRODUCTS_API_URL = getattr(settings, 'LCBO_PRODUCTS_API_URL', 'http://lcboapi.com/products')
