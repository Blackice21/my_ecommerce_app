from django.db import models
from django.db.models import Sum
from django.conf import settings
from books.models import Book

# Create your models here.
class OrderItem(models.Model):
    books = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return self.books.title

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    ref_code = models.CharField(max_length=200, blank=True)
    is_ordered = models.BooleanField(default=False)

    def get_total(self):
        return self.items.all().aggregate(order_total=Sum('books__price'))['order_total']

    def __str__(self):
        return self.user.username

    def track(self):
        return self.items.count    

class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    total = models.FloatField()
    stripe_charge_id = models.CharField(max_length=100)
    date_paid = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.stripe_charge_id