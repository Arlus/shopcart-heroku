from catalog.models import Category
import settings
def shopcart(request):
    return {
        'Categories': Category.objects.filter(is_active=True),
        'site_name': settings.SITE_NAME,
        'request': request
    }


