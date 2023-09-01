from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from estore_cart.models import Cart, CartItems
from estore_app1.models import Product
from django.conf import settings


from django.core.exceptions import ObjectDoesNotExist

import razorpay

from estore_payment.models import Payment


# Create your views here.


def cart_id_creator(request):                                                     # method to create cart_id using session key to be used for creating cart
    cartid_sessionkey = request.session.session_key
    if not cartid_sessionkey:
        cartid_sessionkey = request.session.create()
    return cartid_sessionkey


def add_cart(request, product_id):                                              # view to create cart and add items
    item = get_object_or_404(Product, id=product_id)                            # take product details using product_id
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
        return redirect('estore_cart:cart_details')
    else:
        item.available = False
        item.save()
        return HttpResponse("out of stock")


def cart_details(request, razorpay_amount=0, total=0, counter=0, items=None, order_id=None):
    try:
        bag = Cart.objects.get(cart_id=cart_id_creator(request))                # take already created cart
        print(bag)
        items = CartItems.objects.filter(cart=bag, active=True)           # retrieve all items in the existing cart into "items"
        for i in items:
            total += (i.quantity * i.product.price)                             # grand total
            counter += i.quantity                                               # net quantity
        client = razorpay.Client(auth=(settings.KEY_ID, settings.KEY_SECRET))
        razorpay_amount = int(total) * 100
        data = {"amount": razorpay_amount, "currency": "INR", "receipt": "receipt-" + str(bag)}
        payment = client.order.create(data=data)
        print(payment)
        order_id = payment['id']
        order_status = payment['status']
        if order_status == 'created':
            payment_table_entry = Payment(user=request.user, amount=total, razorpay_order_id=order_id, razorpay_payment_status=order_status)
            payment_table_entry.save()
    except ObjectDoesNotExist:
        pass
    return render(request, 'cart.html', dict(razorpay_amount=razorpay_amount, total=total, counter=counter, items=items, order_id=order_id))


def delete_onebyone(request, product_id):
    item = get_object_or_404(Product, id=product_id)
    try:
        bag = Cart.objects.get(cart_id=cart_id_creator(request))
        cart_item = CartItems.objects.get(product=item, cart=bag)
        if cart_item.quantity > 1:
            cart_item.product.stock += 1
            cart_item.product.save()
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.product.stock += 1
            cart_item.product.save()
            cart_item.delete()

    except ObjectDoesNotExist:
        pass
    return redirect('estore_cart:cart_details')


def delete_all(request, product_id):
    item = get_object_or_404(Product, id=product_id)
    try:
        bag = Cart.objects.get(cart_id=cart_id_creator(request))
        cart_product = CartItems.objects.get(cart=bag, product=item)
        a = cart_product.quantity
        cart_product.delete()
        cart_product.product.stock += a
        cart_product.product.save()
    except ObjectDoesNotExist:
        pass
    return redirect('estore_cart:cart_details')

