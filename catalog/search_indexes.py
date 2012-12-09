from haystack.indexes import *
from haystack import site, indexes, autodiscover
from shopcart.catalog.models import Product


class ProductIndex(indexes.SearchIndex):
    text = indexes.EdgeNgramField(document=True, use_template=True)
    name = CharField(model_attr='name')
    description = CharField(model_attr='description')
    #get_queryset is deprecated
    def index_queryset(self):
        return Product.objects.all()
        
site.register(Product, ProductIndex)

autodiscover()
