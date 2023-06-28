from django.urls import path
from estore_search import views

app_name = 'estore_search'

urlpatterns = [
    path('', views.search_operation, name='search_view'),
]
