from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from estore_app1 import views

app_name = 'estore_app1'
urlpatterns = [
    path('', views.category, name='home'),
    path('<slug:slug_cat>/', views.category, name='category'),
    path('<slug:slug_cat>/<slug:slug_prod>/', views.product, name='product'),

    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)\
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)