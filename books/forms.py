import datetime
from django import forms

from books.models import Book,Author,Genre

#Adding and/or Editing Books
class BookRoomForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = [
            'title',
            'description',
            'publication_year',
            'cover_image',
            'status',
            'rating',
            'author',
            'genres',
        ]

        labels = {
            'title': "Book title",
            'description': "Book description",
            'publication_year': "Publication year",
            'status': "Reading Status",
            'author': "Author",
            'genres': "Genres",

        }

        widgets = {
            'title': forms.TextInput(attrs = {
            'class':"form-control",
            'placeholder': "Enter Book title"
            }),

            'description': forms.Textarea(attrs = {
                'class':"form-control",
                'rows': '1',
                'placeholder': "Write a brief summary of the book..."
            }),

            'cover_image': forms.FileInput(attrs={
                'class': "d-none",
                'id': 'id_cover_image',
                'accept': "image/*"
            }),

            'publication_year': forms.NumberInput(attrs={
                'class': "form-control",
                "min": '1800',
                'max': str(datetime.datetime.now().year),
            }),

            'status': forms.Select(attrs = {
                'class': 'form-select',
            }),

            'rating': forms.NumberInput(attrs = {
                'class': 'form-control',
                'min': '1',
                'max': '5',
                'step': '1'
            }),

            'author': forms.Select(attrs ={'class': "form-control"}),

            'genres': forms.CheckboxSelectMultiple()
        }

    def clean_publication_year(self):
        year = self.cleaned_data['publication_year']
        current_year = datetime.datetime.now().today().year

        if year and year > current_year:
            raise forms.ValidationError('The publication cannot be later than the current year')
        return year

    def clean_rating(self):
        rating = self.cleaned_data['rating']
        if rating is not None and (rating < 1 or rating > 5):
            raise forms.ValidationError('The rating must be between 1 and 5')
        return rating


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = [
            'name',
            'biography',
            'birth_year',
        ]

        widgets = {
            'name': forms.TextInput(attrs = {
            'class':"form-control",
            'placeholder': "Enter Author's name",

            }),

            'biography': forms.Textarea(attrs = {
                'class': "form-control",
                'rows': '1',
                'placeholder': "Write a brief biography about the book..."
            }),

            'birth_year': forms.NumberInput(attrs = {
                'class': "form-control",
                'placeholder':"Enter birth year of the Author"
            })
        }

    def clean_birth_year(self):
        year = self.cleaned_data['birth_year']
        current_year = datetime.datetime.now().year

        if year and year > current_year:
            raise forms.ValidationError('The birth year cannot be in the future')
        return year

class GenreForm(forms.ModelForm):

    class Meta:
        model = Genre
        fields = [
            'name',
            'description',
        ]

        widgets = {
            'name': forms.TextInput(attrs={
                'class': "form-control",
                'placeholder': "Enter Genre's name"
            }),
        }



