from django.shortcuts import render
from .models import Book
# Create your views here.
def home(request):
    book_list = Book.objects.all()
    context = {
        'book_list': book_list
    }
    return render(request, 'book_list.html', context)