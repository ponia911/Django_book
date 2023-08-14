from django.urls import path

from manager.views import AddLikeView, BookView, DetailBook, AddBook

urlpatterns = [
    path('', BookView.as_view(), name='list_view'),
    path('add_like/<int:book_id>', AddLikeView.as_view(), name='add_like'),
    path('detail_book/<int:book_id>', DetailBook.as_view(), name='detail_book'),
    path('add_book/', AddBook.as_view(), name='add_book'),

]