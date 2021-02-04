from django.urls import path
from . import views

urlpatterns = [
    path('add_to_cart/<book_slug>/', views.Add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<book_slug>/', views.Remove_from_cart, name='remove_from_cart'),
    path('order_summary/', views.Order_summary, name='order_summary')
]