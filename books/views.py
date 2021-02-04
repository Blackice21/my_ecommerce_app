from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Chapter, Exercise
from django.http import Http404
from shopping_cart.models import Order, OrderItem
# Create your views here.
OWNED = 'owned'
IN_CART = 'in_cart'
NOT_IN_CART = 'not_in_cart'


def check_book_relationship(request, book):
    if book in request.user.userlibrary.books.all():
        return OWNED
    order_qs = Order.objects.filter(user=request.user)
    if order_qs.exists():
        order = order_qs[0]
        order_item_qs = OrderItem.objects.filter(books=book)
        if order_item_qs.exists():
            order_item = order_item_qs[0]
            if order_item in order.items.all():
                return IN_CART
    return NOT_IN_CART

def book_list(request):
    book_list = Book.objects.all()
    
    try:
        order = Order.objects.get(user=request.user)
    except Order.DoesNotExist:
        order = None

    tr = order.track()
    context = {
        'book_list': book_list,
        'tr':tr
    }
    return render(request, 'book_list.html', context)

def book_detail(request, slug):
    book = get_object_or_404(Book, slug=slug)
    book_status = check_book_relationship(request, book=book)

    try:
        order = Order.objects.get(user=request.user)
        order_item = OrderItem.objects.get(books=book)
        if order_item in order.items.all():
            book_is_in_cart = True
    except Order.DoesNotExist:
        order = None
    except OrderItem.DoesNotExist:
        order_item = None
    
    tr = order.track()
    context = {
        'book': book,
        'book_status':book_status,
        'tr': tr
    }
    return render(request, 'book_detail.html', context)

def chapter_detail(request, book_slug, chapter_number):
    chapters = Chapter.objects \
              .filter(book__slug=book_slug) \
              .filter(chapter_number=chapter_number)

    chapter = chapters[0]

    try:
        order = Order.objects.get(user=request.user)
    except Order.DoesNotExist:
        order = None

    tr = order.track()
    book_status = check_book_relationship(request, book=chapter.book)
    if chapters.exists():
        context={
            'chapter': chapter,
            'book_status': book_status,
            'tr': tr,
            }
        return render(request, 'chapter_detail.html', context)
    raise Http404

def exercise_detail(request, book_slug, chapter_number, chapter_title, ex_number):
    ex_qs = Exercise.objects \
              .filter(chapter__book__slug=book_slug) \
              .filter(chapter__chapter_number=chapter_number) \
              .filter(chapter__title=chapter_title) \
              .filter(exercise_number=ex_number)

    try:
        order = Order.objects.get(user=request.user)
    except Order.DoesNotExist:
        order = None
    
    tr = order.track()
    exercise = ex_qs[0]
    book_status = check_book_relationship(request, book=exercise.chapter.book)
    if ex_qs.exists():
        context={
            'exercise': exercise, 
            'book_status': book_status,
            'tr': tr,}
        return render(request, 'exercise_detail.html', context)
    raise Http404

