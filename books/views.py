from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Chapter, Exercise
from django.http import Http404
from shopping_cart.models import Order, OrderItem
# Create your views here.
def book_list(request):
    book_list = Book.objects.all()
    context = {
        'book_list': book_list
    }
    return render(request, 'book_list.html', context)

def book_detail(request, slug):
    book = get_object_or_404(Book, slug=slug)
    book_is_in_cart = False
    try:
        order = Order.objects.get(user=request.user)
        order_item = OrderItem.objects.get(books=book)
        if order_item in order.items.all():
            book_is_in_cart = True
    except Order.DoesNotExist:
        order = None

    context = {
        'book': book,
        'item': book_is_in_cart
    }
    return render(request, 'book_detail.html', context)

def chapter_detail(request, book_slug, chapter_number):
    chapters = Chapter.objects \
              .filter(book__slug=book_slug) \
              .filter(chapter_number=chapter_number)

    if chapters.exists():
        context={'chapter': chapters[0]}
        return render(request, 'chapter_detail.html', context)
    raise Http404

def exercise_detail(request, book_slug, chapter_number, chapter_title, ex_number):
    ex_qs = Exercise.objects \
              .filter(chapter__book__slug=book_slug) \
              .filter(chapter__chapter_number=chapter_number) \
              .filter(chapter__title=chapter_title) \
              .filter(exercise_number=ex_number)

    if ex_qs.exists():
        context={'exercise': ex_qs[0]}
        return render(request, 'exercise_detail.html', context)
    raise Http404

