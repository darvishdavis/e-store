from django.urls import path
from estore_secure import views

app_name = 'estore_secure'

urlpatterns =[
    path('register/', views.register, name='register'),
    path('', views.log_in, name='login'),
    path('log/out/', views.log_out, name='logout')
]