from django.db import models

from books.models import Book


# Create your models here.

class ReadingGoal(models.Model):
    year = models.PositiveIntegerField(unique=True)
    target_book = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.year} - {self.target_book}"

    def get_completed_count(self):

        """""Counts the books completed in this goal's year and filtering for status 'COMPLETED' """

        return Book.objects.filter(
            completed_at__year = self.year,
            status = Book.StatusChoices.COMPLETED
        ).count()

    def get_progress_in_percentage(self):
        """"" Gives us the progress in percentage """

        if self.target_book == 0:
            return 0
        percentage = (self.get_completed_count() / self.target_book) * 100
        return min(round(percentage), 100)

    @property
    def is_completed(self):
        return self.get_completed_count() >= self.target_book
