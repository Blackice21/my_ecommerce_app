from django.shortcuts import render, get_object_or_404
from .models import Book
# Create your views here.
def book_list(request):
    book_list = Book.objects.all()
    context = {
        'book_list': book_list
    }
    return render(request, 'book_list.html', context)

def book_detail(request, slug):
    book = get_object_or_404(Book, slug=slug)
    context = {
        'book': book
    }
    return render(request, 'book_detail.html', context)


