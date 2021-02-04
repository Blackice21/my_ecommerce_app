from django.shortcuts import render, get_object_or_404
from .models import Order, OrderItem
from books.models import Book
from django.http import  HttpResponseRedirect
# Create your views here.
def Add_to_cart(request, book_slug):
    book = get_object_or_404(Book, slug=book_slug)
    order_item, creation = OrderItem.objects.get_or_create(books=book)
    order, created = Order.objects.get_or_create(user=request.user)
    order.items.add(order_item)
    order.save()
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

def Remove_from_cart(request, book_slug):
    book = get_object_or_404(Book, slug=book_slug)
    order_item = get_object_or_404(OrderItem, books=book)
    order = get_object_or_404(Order, user=request.user)
    order.items.remove(order_item)
    order.save()
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

def Order_summary(request):
     order = get_object_or_404(Order, user=request.user)
     context={
         'order': order
     }
     return render(request, 'order_summary.html', context)