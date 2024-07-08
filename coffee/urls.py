# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('checkout/', views.checkout, name='checkout'),
    path('add_to_cart/<int:coffee_id>/', views.add_to_cart, name='add_to_cart')
]
