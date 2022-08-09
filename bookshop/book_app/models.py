from django.db import models

# Create your models here.


class Book(models.Model):
    author = models.CharField(max_length=40)
    title = models.CharField(max_length=100, null=True)
    rating = models.IntegerField()
    is_best_selling = models.BooleanField()

    def __str__(self):
        return f"{self.author} - '{self.title}' - {self.rating}% - {'bestseller' if self.is_best_selling else 'not bestseller'}"

