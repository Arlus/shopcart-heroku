from django.conf.urls.defaults import patterns, include, url
from catalog import views

urlpatterns = patterns('',
               url(r'^$', views.home, name='catalog_home'),
               url(r'^category/(?P<category_slug>[-\w]+)/$',
views.show_category, {
'template_name':'catalog/category.html'},'catalog_category'),
               url(r'^product/(?P<product_slug>[-\w]+)/$',
views.show_product, {
'template_name':'catalog/product.html'},'catalog_product'),
               url(r'^new/$', views.new_product, {'template_name':'catalog/new.html'}, 'new_product'),

)
