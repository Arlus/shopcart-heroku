from shopcart.catalog.models import Category
from shopcart import settings
def shopcart(request):
    return {
        'Categories': Category.objects.filter(is_active=True),
        'site_name': settings.SITE_NAME,
        'request': request
    }


