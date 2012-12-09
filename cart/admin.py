from django.contrib import admin
from models import CartItem

class CartItemAdmin(admin.ModelAdmin):
   list_display = ('cart_id', 'quantity', 'product',) 

admin.site.register(CartItem, CartItemAdmin)
