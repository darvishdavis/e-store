from django.urls import path
from estore_cart import views

app_name = 'estore_cart'

urlpatterns = [
    path('your/cart', views.cart_details, name='cart_details'),
    path('add-cart/<int:product_id>/', views.add_cart, name='add_cart'),
    path('delete/<int:product_id>/', views.delete_onebyone, name='delete_onebyone'),
    path('delete-product/<int:product_id>/', views.delete_all, name='delete_all'),


]