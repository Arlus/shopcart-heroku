# Create your views here.
from django.shortcuts import render_to_response
from models import Product, Category
from django.template import RequestContext
from forms import productForm
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
import datetime
from cart.forms import ProductAddToCartForm
from cart import cart
from django.core import urlresolvers
from django import forms
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# encoding: utf-8

def home(request):
    pros = Product.objects.all()
    paginator = Paginator(pros, 10)
    page = request.GET.get('page','1')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    categories = Category.objects.all()
    page_title = "Shopcart - Home"
    if request.method == 'POST':
        # add to cart...create the bound form
        postdata = request.POST.copy()
        form = ProductAddToCartForm(request, postdata)
        #check if posted data is valid
        if form.is_valid():
            #add to cart and redirect to cart page
            cart.add_to_cart(request)
            # if test cookie worked, get rid of it
            if request.session.test_cookie_worked():
                request.session.delete_test_cookie()
            url = urlresolvers.reverse('show_cart')
            return HttpResponseRedirect(url)
    else:
        
        form = ProductAddToCartForm(request=request, initial={'quantity':1}, label_suffix=':')
        form.fields['quantity'].widget = forms.HiddenInput()
    # set the test cookie on our first GET request
    request.session.set_test_cookie()    
    return render_to_response('index.html', ({'products' : products, 'categories':categories}),context_instance=RequestContext(request)
)

def show_category(request, category_slug, template_name="catalog/category.html"):
    c = get_object_or_404(Category, slug=category_slug)
    products = c.product_set.all()
    page_title = c.name
    meta_keywords = c.meta_keywords
    meta_description = c.meta_description
    if request.method == 'POST':
    # add to cart...create the bound form
        postdata = request.POST.copy()
        form = ProductAddToCartForm(request, postdata)
        #check if posted data is valid
        if form.is_valid():
            #add to cart and redirect to cart page
            cart.add_to_cart(request)
            # if test cookie worked, get rid of it
            if request.session.test_cookie_worked():
                request.session.delete_test_cookie()
                url = urlresolvers.reverse('show_cart')
                return HttpResponseRedirect(url)
    else:
        form = ProductAddToCartForm(request=request, initial={'quantity':1}, label_suffix=':')
        form.fields['quantity'].widget = forms.HiddenInput()    
    return render_to_response(template_name, locals(),context_instance=RequestContext(request))

# new product view, with POST vs GET detection
def show_product(request, product_slug, template_name="catalog/product.html"):
    product = get_object_or_404(Product, slug=product_slug)
    categories = Category.objects.all()
    cats = product.categories.all()
    page_title = product.name
    meta_keywords = product.meta_keywords
    meta_description = product.meta_description
    # need to evaluate the HTTP method
    if request.method == 'POST':
        # add to cart...create the bound form
        postdata = request.POST.copy()
        form = ProductAddToCartForm(request, postdata)
        #check if posted data is valid
        if form.is_valid():
            #add to cart and redirect to cart page
            cart.add_to_cart(request)
            # if test cookie worked, get rid of it
            if request.session.test_cookie_worked():
                request.session.delete_test_cookie()
            url = urlresolvers.reverse('show_cart')
            return HttpResponseRedirect(url)
    else:
        
        form = ProductAddToCartForm(request=request, initial={'quantity':1}, label_suffix=':')
        form.fields['quantity'].widget = forms.HiddenInput()
    # assign the hidden input the product slug
    form.fields['product_slug'].widget.attrs['value'] = product_slug
    # set the test cookie on our first GET request
    request.session.set_test_cookie()
    return render_to_response("catalog/product.html", locals(),
context_instance=RequestContext(request))


def new_product(request, template_name="catalog/new.html"):
    categories = Category.objects.all()
    product = Product()
    if request.user.is_authenticated():
        if request.method == "POST":
            form = productForm(request.POST, request.FILES)
            if form.is_valid():
                saves = Product(name=request.POST['name'], price=request.POST['price'], old_price=request.POST['old_price'], quantity=request.POST['quantity'], description=request.POST['description'], meta_keywords=request.POST['name'].split(), image=request.FILES['photo'], meta_description="none", created_at=datetime.datetime.now(), updated_at=datetime.datetime.now(), is_bestseller=True, is_active=True, is_featured=True, user = request.user, slug = request.POST['name'].strip().replace(' ', '_').lower())
            
                saves.save()
                for c in request.POST.getlist('categories'):
                    saves.categories.add(c)
                return HttpResponseRedirect('/')            
        else:
            form = productForm()
    else:
        return HttpResponseRedirect('/accounts/login/')
    return render_to_response(template_name, {'form':form, 'categories':categories,}, context_instance=RequestContext(request))
        
