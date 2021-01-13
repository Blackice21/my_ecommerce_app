from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('<slug>', views.book_detail, name='book_detail'),
    path('<book_slug>/<int:chapter_number>', views.chapter_detail, name='chapter_detail'),
    path('<book_slug>/<int:chapter_number>/<chapter_title>/<int:ex_number>', views.exercise_detail, name='exercise_detail'),
]