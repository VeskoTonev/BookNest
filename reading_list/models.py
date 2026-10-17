from django.db import models

from books.models import Book


# Create your models here.

class ReadingList(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class ReadingListItems(models.Model):
    reading_list = models.ForeignKey(ReadingList, on_delete=models.CASCADE, related_name = 'items')
    book = models.ForeignKey(Book, on_delete=models.CASCADE,related_name = 'reading_list_items')
    added_at = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True)

    class Meta:

        constraints = [
            models.UniqueConstraint(
                fields = ['reading_list', 'book'],
                name = 'unique_per_book_reading_list'
            )
        ]

    def __str__(self):
        return f"{self.book} in {self.reading_list}"

