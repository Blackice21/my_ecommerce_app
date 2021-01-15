from django.db import models
from django.shortcuts import redirect, reverse
from django.conf import settings
from django.db.models.signals import  post_save
# Create your models here.
'''author
    book
        chapter
            excercise
                solution1'''

class UserLibrary(models.Model):
    books = models.ManyToManyField('Book')
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username   

    def get_books(self):
        return self.books.all()

    class Meta:
        verbose_name = 'User Library'
        verbose_name_plural = 'User Library'

def post_user_signup_receiver(sender, instance, created, *args, **kwargs):
    if created:
        UserLibrary.objects.get_or_create(user=instance)

post_save.connect(post_user_signup_receiver, sender=settings.AUTH_USER_MODEL)

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    slug = models.SlugField(default=first_name)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ManyToManyField(Author)
    isbn = models.CharField(max_length=16)
    slug = models.SlugField(default=title)
    pub_date = models.DateField(auto_now=True)
    price = models.FloatField()
    cover = models.ImageField()

    def __str__(self):
        return self.title
    
    #def get_absolute_url(self):
        #from django.core.urlresolvers import reverse
     #   return redirect(reverse('book_list'))
    def get_absolute_url(self):
        #djanfromgo.core.urlresolvers import reverse
        return reverse('book_detail', kwargs={'slug': self.slug})

class Chapter(models.Model):
    title = models.CharField(max_length=100)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    chapter_number = models.IntegerField()

    def __str__(self):
         return self.title

    def get_absolute_url(self):
        #djanfromgo.core.urlresolvers import reverse
        return reverse('chapter_detail', kwargs={
            'book_slug': self.book.slug,
            'chapter_number': self.chapter_number
            })
     

class Exercise(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    exercise_number = models.IntegerField()
    pg_number = models.IntegerField()

    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        return reverse('exercise_detail', kwargs={
                'book_slug': self.chapter.book.slug,
                'chapter_number': self.chapter.chapter_number,
                'chapter_title': self.chapter.title,
                'ex_number': self.exercise_number
                })

class Solution(models.Model):
    sol_number = models.IntegerField(default=1)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    image = models.ImageField()

    def __str__(self):
         return f"{self.exercise}--{self.pk}"
    # solution = models.TextField()