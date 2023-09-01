from django.contrib import admin

from estore_payment.models import Payment, OrderPlaced


# Register your models here.

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['user', 'paid']


@admin.register(OrderPlaced)
class OrderPlacedAdmin(admin.ModelAdmin):
    list_display = ['user', 'products', 'quantity', 'status', 'payment']
