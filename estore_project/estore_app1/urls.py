
from django.urls import path
from estore_app1 import views

app_name = 'estore_app1'
urlpatterns = [
    path('home/', views.category, name='home'),
    path('<slug:slug_cat>/', views.category, name='category'),
    path('<slug:slug_cat>/<slug:slug_prod>/', views.product, name='product'),

    ]