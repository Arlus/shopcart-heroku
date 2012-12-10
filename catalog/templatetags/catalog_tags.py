from django import template
import cart.cart import cart_distinct_item_count
from catalog.models import Category

register = template.Library()

@register.inclusion_tag("tags/cart_box.html")

def cart_box(request):
    cart_item_count = cart_distinct_item_count(request)
    return {'cart_item_count': cart_item_count }

@register.inclusion_tag("tags/category_list.html")  
def category_list(request_path):
    active_categories = Category.objects.all()
    return {
            'active_categories': active_categories,
            'request_path': request_path
            }
