from django.shortcuts import render, redirect

from estore_cart.models import Cart, CartItems
from estore_cart.views import cart_id_creator
from estore_payment.models import Payment, OrderPlaced


# Create your views here.


def payment(request):                                       # view for storing payment details, fetching cart details & deleting existing carts
    order_id = request.GET.get('order_id')
    payment_id = request.GET.get('payment_id')
    # print(payment_id, " ", order_id)
    payment_details = Payment.objects.get(razorpay_order_id=order_id)
    payment_details.paid = True
    payment_details.razorpay_payment_id = payment_id
    payment_details.save()                                    # update payment table
    user = request.user
    bag = Cart.objects.get(cart_id=cart_id_creator(request))  # fetching cart details
    # print(bag)
    cart_items = CartItems.objects.filter(cart=bag)            # fetching cart items
    for item in cart_items:
        # print(item)
        OrderPlaced(user=user, cart=bag, products=item.product, quantity=item.quantity, payment=payment_details).save()   # update OrderPlaced table
        item.delete()
    bag.delete()                                               #    delete cart details

    return redirect('estore_payment:orders')


def order(request):
    placed_orders = OrderPlaced.objects.filter(cart=cart_id_creator(request))
    return render(request, 'order.html', {'placed_orders': placed_orders})
