from django.urls import path
from . import views

urlpatterns = [
    path('add_to_cart/<book_slug>/', views.Add_to_cart, name='add_to_cart')
]