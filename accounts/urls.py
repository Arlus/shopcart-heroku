from django.conf.urls.defaults import *
from shopcart import settings

urlpatterns = patterns('shopcart.accounts.views',
(r'^register/$', 'register',
{'template_name': 'registration/register.html'},
'register'),
#(r'^my_account/$', 'my_account',
#{'template_name': 'registration/my_account.html'}, 'my_account'),
#(r'^order_details/(?P<order_id>[-\w]+)/$', 'order_details',
#{'template_name': 'registration/order_details.html'}, 'order_details'),
#(r'^order_info//$', 'order_info',
#{'template_name': 'registration/order_info.html'}, 'order_info'),
)
urlpatterns += patterns('django.contrib.auth.views',
(r'^login/$', 'login',
{'template_name': 'registration/login.html'}, 'login'),
(r'^logout/$', 'logout',
{'template_name': 'registration/logged_out.html'}, 'logout'),
)

