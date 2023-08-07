from django.urls import path

from manager.views import AddLikeView, BookView

urlpatterns = [
    path('', BookView.as_view(), name='list_view'),
    path('add_like/<int:book_id>', AddLikeView.as_view(), name='add_like'),

]