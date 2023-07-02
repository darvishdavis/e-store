from django.urls import path
from estore_cart import views

app_name = 'estore_cart'

urlpatterns = [
    path('<int:product_id>/', views.add_cart, name='add_cart'),
    #path('cart_details/', views.cart_details, name='cart_details'),

]