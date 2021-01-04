from django.db import models

# Create your models here.
'''author
    book
        chapter
            excercise
                solution1'''

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    slug = models.SlugField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ManyToManyField(Author)
    isbn = models.CharField(max_length=16)
    slug = models.SlugField()
    pub_date = models.DateField(auto_now=True)
    price = models.FloatField()
    cover = models.ImageField()

    def __str__(self):
        return self.title

class Chapter(models.Model):
    title = models.CharField(max_length=100)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    chapter_number = models.IntegerField()

    def __str__(self):
         return self.title

class Exercise(models.Model):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    exercise_number = models.IntegerField()
    pg_number = models.IntegerField()

    def __str__(self):
        return self.title

class Solution(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    image = models.ImageField()

    def __str__(self):
         return f"{self.exercise}--{self.pk}"
    # solution = models.TextField()