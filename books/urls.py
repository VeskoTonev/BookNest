from django.urls import path

from books import views

app_name = 'books'
urlpatterns = [
    # Book Routes
    path('', views.BookListView.as_view(), name = 'book_list' ),
    path('add/', views.BookCreateView.as_view(), name='book_add'),
    path('<int:pk>/', views.BookDetailsView.as_view(), name = 'book_details'),
    path('<int:pk>/update/', views.BookUpdateView.as_view(), name = 'book_update'),
    path('<int:pk>/delete/', views.BookDeleteView.as_view(), name = 'book_delete' ),

    # Author Routes

    path('authors/', views.AuthorListView.as_view(), name = 'author_list'),
    path('authors/add/', views.AuthorCreateView.as_view(), name = 'author_add'),
    path('authors/<int:pk>/', views.AuthorDetailsView.as_view(), name = 'author_details'),
    path('authors/<int:pk>/update/', views.AuthorUpdateView.as_view(), name = 'author_update'),
    path('author/<int:pk>/delete/', views.AuthorDeleteView.as_view(), name = 'author_delete'),

    # Genre Routes

    path('genres/', views.GenreListView.as_view(), name = 'genre_list'),
    path('genres/add/', views.GenreCreateView.as_view(), name = 'genre_add'),
    path('genres/<int:pk>/', views.GenreDetailsView.as_view(), name = 'genre_details'),
    path('genres/<int:pk>/update/', views.GenreUpdateView.as_view(), name = 'genre_update'),
    path('genres/<int:pk>/delete/', views.GenreDeleteView.as_view(), name = 'genre_delete')

]