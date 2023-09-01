from django.contrib.auth.models import User
from django.db import models

from estore_app1.models import Product


# Create your models here.

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.IntegerField()
    razorpay_order_id = models.CharField(max_length=100, null=True)
    razorpay_payment_status = models.CharField(max_length=50, null=True)
    razorpay_payment_id = models.CharField(max_length=100, null=True)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user}"


status_choices = (('Packed', 'Packed'), ('On The Way', 'On The Way'), ('Delivered', 'Delivered'),
                  ('Accepted', 'Accepted'), ('Pending', 'Pending'), ('Cancel', 'Cancel'))


class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.CharField(max_length=100, default='empty')
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=status_choices, default='Pending')
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.cart}"


