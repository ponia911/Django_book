from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse
from django.views.generic import ListView
from manager.models import Book, Comment
from django.db.models import Count
from django.db.models import Prefetch
class BookView(View):
    def get(self, request):
        comments_for_prefetch = Prefetch('comments', queryset=Comment.objects.annotate(likes_comments=Count('likes')))
        data = {'books': Book.objects.
        prefetch_related('comments', 'authors').
                annotate(likes_book=Count('likes'))}
        return render(request,'index.html', context=data)

#     {% if books.comments.exists %}
#         <h4> Comments </h4>
#         {{ for comment in books.comments }}
#         <h5>{{ comment.text }}</h5>
#     {% endif %}
# {% endfor %}
class AddLikeView(View):
    def get(self, request, book_id):
        print(request.user, type(request.user))
        if request.user.is_authenticated:
            book = Book.objects.get(id=book_id)
            if request.user in book.likes.all():
                book.likes.remove(request.user)
            else:
                book.likes.add(request.user)


        return redirect('list_view')