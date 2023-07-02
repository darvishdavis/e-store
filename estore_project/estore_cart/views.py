from django.http import HttpResponse
from django.shortcuts import render, redirect
from estore_cart.models import Cart, CartItems
from estore_app1.models import Product

from django.core.exceptions import ObjectDoesNotExist


# Create your views here.

def cart_id_creator(request):                                                     # method to create cart_id using session key to be used for creating cart
    cartid_sessionkey = request.session.session_key
    if not cartid_sessionkey:
        cartid_sessionkey = request.session.create()
    return cartid_sessionkey


# def add_cart(request, product_id):                                              # view to create cart and add items
#     item = Product.objects.get(id=product_id)                                   # take product details using product_id
#     try:
#         bag = Cart.objects.get(cart_id=cart_id_creator(request))                # assign already created cart
#     except ObjectDoesNotExist:
#         bag = Cart.objects.create(cart_id=cart_id_creator(request))             # create cart
#         bag.save()
#
#     try:
#         cart_item = CartItems.objects.get(product=item, cart=bag)               # add item (using product=item, cart=bag ) into created cart
#         cart_item.quantity += 1
#         cart_item.save()
#     except ObjectDoesNotExist:
#         cart_item = CartItems.objects.create(product=item, cart=bag, quantity=1)    # create item (using product=item, cart=bag ) into created cart
#         cart_item.save()
#     return redirect('estore_cart:cart_details')
#
#
# def cart_details(request, total=0, counter=0, items=None):
#     try:
#         bag = Cart.objects.get(cart_id=cart_id_creator(request))                # assign already created cart
#         items = CartItems.objects.all().filter(cart=bag, active=True)           # retrieve all items in the existing cart into "items"
#         for i in items:
#             total += (i.quantity * i.product.price)                             # grand total
#             counter += i.quantity                                              # net quantity
#     except ObjectDoesNotExist:
#         pass
#     return render(request, 'cart.html', dict(total=total, counter=counter, items=items))


def add_cart(request, product_id, total=0, counter=0, items=None):              # view to create cart and add items
    item = Product.objects.get(id=product_id)                                   # take product details using product_id
    item.stock -= 1
    item.save()
    if item.stock > 0:
        try:
            bag = Cart.objects.get(cart_id=cart_id_creator(request))                # assign already created cart
        except ObjectDoesNotExist:
            bag = Cart.objects.create(cart_id=cart_id_creator(request))             # create cart
            bag.save()

        try:
            cart_item = CartItems.objects.get(product=item, cart=bag)               # add item (using product=item, cart=bag ) into created cart
            cart_item.quantity += 1
            cart_item.save()
        except ObjectDoesNotExist:
            cart_item = CartItems.objects.create(product=item, cart=bag, quantity=1)    # create item (using product=item, cart=bag ) into created cart
            cart_item.save()

        try:
            items = CartItems.objects.all().filter(cart=bag, active=True)           # retrieve all items in the existing cart into "items"
            for i in items:
                total += (i.quantity * i.product.price)                             # grand total
                counter += i.quantity                                               # net quantity
        except ObjectDoesNotExist:
            pass

    else:
        return HttpResponse("out of stock")

    return render(request, 'cart.html', dict(total=total, counter=counter, items=items))
