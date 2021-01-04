from django.contrib import admin
from .models import Book, Author, Chapter, Exercise, Solution
# Register your models here.
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Chapter)
admin.site.register(Exercise)
admin.site.register(Solution)