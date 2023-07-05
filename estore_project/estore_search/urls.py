from django.urls import path, include
from estore_search import views

app_name = 'estore_search'

urlpatterns = [
    path('here/and-there', views.search_operation, name='search_view'),

]