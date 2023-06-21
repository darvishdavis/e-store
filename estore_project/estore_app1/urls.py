from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from estore_app1 import views

app_name = 'estore_app1'
urlpatterns = [
    path('', views.home, name='home'),
    path('<slug:slug_cat>/', views.category, name='ctgry'),

    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)