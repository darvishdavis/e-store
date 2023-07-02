from django.contrib import admin
from .models import Cart, CartItems
# Register your models here.


class RegisterCart(admin.ModelAdmin):
    list_display = ['cart_id', 'created_date']


admin.site.register(Cart, RegisterCart)


class RegisterCartItems(admin.ModelAdmin):
    list_display = ['product', 'cart', 'quantity', 'active']
    list_editable = ['quantity', 'active']


admin.site.register(CartItems, RegisterCartItems)
