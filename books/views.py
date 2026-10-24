from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from books.forms import BookRoomForm, AuthorForm, GenreForm
from books.models import Book, Author, Genre


# Create your views here.

#Views for books

class BookListView(ListView):
    model = Book
    template_name = "books/book_list.html"
    context_object_name = "books"
    ordering = ['title']

class BookDetailsView(DetailView):
    model = Book
    template_name = "books/book_detail.html"
    context_object_name = 'book'

class BookCreateView(SuccessMessageMixin, CreateView):
    model = Book
    form_class = BookRoomForm
    template_name = "books/book_form.html"
    success_message = "Book's saved successfully"

    def get_success_url(self):

        return reverse("books:book-details",kwargs = {"pk": self.object.pk})


class BookUpdateView(SuccessMessageMixin, UpdateView):
    model = Book
    form_class = BookRoomForm
    template_name = "books/book_form.html"
    success_message = "Book's updated successfully"

    def get_success_url(self):
        return reverse("books:book-details", kwargs = {"pk": self.object.pk})

class BookDeleteView(SuccessMessageMixin, DeleteView):
    model = Book
    template_name = "books/book_confirm_delete.html"
    context_object_name = 'book'
    success_url = reverse_lazy("books:book_list")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Book's deleted successfully")
        return super().delete(request, *args, **kwargs)


# Views for Authors

class AuthorListView(ListView):
    model = Author
    template_name = "author_and_genres/author_detail.html"
    context_object_name = "authors"
    ordering = ['name']

class AuthorDetailsView(DetailView):
    model = Author
    template_name = "author_and_genres/author_detail.html"
    context_object_name = "author"

class AuthorCreateView(SuccessMessageMixin, CreateView):
    model = Author
    form_class = AuthorForm
    template_name = "author_and_genres/author_form.html"
    success_message = "Author's saved successfully"

    def get_success_url(self):
        return reverse_lazy("books:author_details", kwargs = {"pk": self.object.pk})


class AuthorUpdateView(SuccessMessageMixin, UpdateView):
    model = Author
    form_class = AuthorForm
    template_name = "author_and_genres/author_form.html"
    success_message = "Author's updated successfully"

    def get_success_url(self):
        return reverse_lazy("books:author_detail", kwargs = {"pk": self.object.pk})

class AuthorDeleteView(SuccessMessageMixin, DeleteView):
    model = Author
    template_name = "author_and_genres/author_confirm_delete.html"
    context_object_name = 'author'
    success_url = reverse_lazy("books:author_list")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Author deleted successfully")
        return super().delete(request, *args, **kwargs)

# Views for genres

class GenreListView(ListView):
    model = Genre
    template_name = "author_and_genres/genre_list.html"
    context_object_name = "genre"
    ordering = ['name']

class GenreDetailsView(DetailView):
    model = Genre
    template_name = "author_and_genres/genre_detail.html"
    context_object_name = "genre"

class GenreCreateView(SuccessMessageMixin, CreateView):
    model = Genre
    form_class = GenreForm
    template_name = "author_and_genres/genre_form.html"
    success_message = "Genre's saved successfully"

    def get_success_url(self):
        return reverse_lazy("books:genre_detail", kwargs = {"pk": self.object.pk})

class GenreUpdateView(SuccessMessageMixin, UpdateView):
    model = Genre
    form_class = GenreForm
    template_name = "author_and_genres/genre_form.html"
    success_message = "Genre's updated successfully"

    def get_success_url(self):
        return reverse_lazy("books:genre_detail", kwargs = {"pk": self.object.pk})

class GenreDeleteView(SuccessMessageMixin, DeleteView):
    model = Genre
    template_name = "author_and_genres/genre_confirm_delete.html"
    context_object_name = 'genre'
    success_url = reverse_lazy("books:genre_list")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Genre deleted successfully")
        return super().delete(request, *args, **kwargs)
