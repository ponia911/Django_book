from django.urls import path

from manager.views import AddLikeView, BookView, DetailBook, AddBook, delete_book, UpdateBook, Login, Register, \
    logout_func

urlpatterns = [
    path('', BookView.as_view(), name='list_view'),
    path('add_like/<int:book_id>/<int:location>', AddLikeView.as_view(), name='add_like'),
    path('detail_book/<int:book_id>', DetailBook.as_view(), name='detail_book'),
    path('add_book/', AddBook.as_view(), name='add_book'),
    path('delete_book/<int:book_id>/', delete_book, name='delete_book'),
    path('update_book/<int:book_id>/', UpdateBook.as_view(), name='update_book'),
    path('login/', Login.as_view(), name='login'),
    path('register/', Register.as_view(), name='register'),
    path('logout/', logout_func, name='logout'),
]

