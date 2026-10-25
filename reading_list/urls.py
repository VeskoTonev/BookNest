from django.urls import path
from . import views

app_name = 'reading_list'
urlpatterns = [
    path('', views.ReadingListView.as_view(), name='list'),
    path('new/', views.ReadingListCreateView.as_view(), name='create'),
    path('<int:pk>/', views.ReadingListDetailsView.as_view(), name='detail'),
    path('reading-lists/<int:pk>/edit/', views.ReadingListUpdateView.as_view(), name='reading_list_update'),
    path('<int:pk>/delete/', views.ReadingListDeleteView.as_view(), name='list_delete'),
    path('item/<int:pk>/delete/', views.ReadingItemListDeleteView.as_view(), name='item_delete'),
]