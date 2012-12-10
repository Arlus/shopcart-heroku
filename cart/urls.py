#cart urls...included in the root projects urls
from django.conf.urls.defaults import *
import views

urlpatterns = patterns('',
(r'^$', views.show_cart, { 'template_name': 'cart/cart.html' }, 'show_cart'),
)

