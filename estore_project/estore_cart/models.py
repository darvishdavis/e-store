from django.db import models
from estore_app1.models import Product


# Create your models here.


class Cart(models.Model):
    cart_id = models.CharField(max_length=250, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "cart"
        ordering = ["created_date"]

    def __str__(self):
        return '{}' .format(self.cart_id)


class CartItems(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=True)
    active = models.BooleanField(default=True)

    class Meta:
        db_table = "cart_items"

    def total(self):
        return self.quantity * self.product.price

    def __str__(self):
        return '{}' .format(self.product)