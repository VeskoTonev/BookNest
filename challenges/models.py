from django.db import models

from books.models import Book


# Create your models here.

class ReadingGoal(models.Model):
    year = models.PositiveIntegerField(unique=True)
    target_book = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.year} - {self.target_book}"