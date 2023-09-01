from django.urls import path
from estore_payment import views

app_name = 'estore_payment'

urlpatterns = [
    path('your-payments/', views.payment, name='payments'),
    path('your-orders/', views.order, name='orders')
]
