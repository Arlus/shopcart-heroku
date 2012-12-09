from django.conf.urls.defaults import *
from django.views.static import serve
from django.conf import settings
import os.path
import catalog
import cart


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'catalog.views.home'),
    (r'^catalog/', include('catalog.urls')),
    (r'^cart/', include('cart.urls')),
    (r'^accounts/', include('accounts.urls')),
    (r'^search/', include('haystack.urls')),

    # Examples:
    # url(r'^$', 'shopcart.views.home', name='home'),
    # url(r'^shopcart/', include('shopcart.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )
