from django.urls import path
from .views import (
    BookListView, BookDetailView,
)

app_name = 'books'
urlpatterns = [
    path('book_list/', BookListView.as_view(), name='book_list'),
    path('book_detail/<int:pk>', BookDetailView.as_view(), name='book_detail'),
]