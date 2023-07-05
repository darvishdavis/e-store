from django.core.exceptions import ObjectDoesNotExist

from estore_cart.views import cart_id_creator
from .models import Cart, CartItems


def cart_quantity(request, total_quantity=0):
    if 'admin' in request.path:
        return {}
    else:
        try:
            bag = Cart.objects.filter(cart_id=cart_id_creator(request))
            items = CartItems.objects.filter(cart=bag[:1])
            for i in items:
                total_quantity += i.quantity
        except ObjectDoesNotExist:
            total_quantity = 0
    return dict(quantity=total_quantity)
