from django.db import models
from django.db.models import ForeignKey
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
# Includes book details, an author and genres.

class Book(models.Model):


    class StatusChoices(models.TextChoices):
        WANT_TO_READ = "want_to_read", "want to read"
        COMPLETED = "completed", "Completed"
        ON_HOLD = "on_hold", "On hold"
        DROPPED = "dropped", "Dropped"
        CURRENTLY_READING = "currently_reading","Currently reading"


    title = models.CharField(max_length=150)
    description = models.TextField()
    publication_year = models.PositiveIntegerField()

    status = models.CharField(max_length=30,
                              choices=StatusChoices.choices,
                              default = StatusChoices.WANT_TO_READ)
    rating = models.PositiveIntegerField(null=True, blank=True,validators=[
                                                                     MinValueValidator(1),
                                                                     MaxValueValidator(5)])
    completed_at = models.DateTimeField(null=True, blank=True)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    genres = models.ManyToManyField('Genre', related_name='books')
    cover_image = models.ImageField(upload_to = 'books_covers/', null = True, blank = True)

    def __str__(self):
        return self.title

    # Stores the author's name, biography and birth year.
class Author(models.Model):
    name = models.CharField(max_length=150)
    biography = models.TextField()
    birth_year = models.IntegerField()


    def __str__(self):
        return self.name

#
class Genre(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return self.name