from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.db.models import Count, Prefetch
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView

from manager.forms import AddBookForm
from manager.models import Book, Comment


class BookView(View):

    def get(self, request):
        comments_for_prefetch = Prefetch('comments',
                                         queryset=Comment.objects.
                                         select_related('user').
                                         annotate(likes_comment=Count('likes'))
                                         )
        data = {'books': Book.objects.
        prefetch_related(comments_for_prefetch, 'authors').all().order_by('-count_likes', 'date')
                # annotate(likes_book=Count('likes'))
                }
        # data = {'books': Book.objects.all()}
        return render(request, 'index.html', context=data)


class AddLikeView(View):
    def get(self, request, book_id, location):
        if request.user.is_authenticated:
            book = Book.objects.get(id=book_id)
            if request.user in book.likes.all():
                book.likes.remove(request.user)
                book.count_likes -= 1
            else:
                book.likes.add(request.user)
                book.count_likes += 1
            book.save()
        if location:
            return redirect('detail_book', book_id=book_id)
        return redirect('list_view')


class DetailBook(View):
    def get(self, request, book_id):
        comments_for_prefetch = Prefetch('comments',
                                         queryset=Comment.objects.
                                         select_related('user').
                                         annotate(likes_comment=Count('likes'))
                                         )
        book = (Book.objects.filter(id=book_id).
                prefetch_related(comments_for_prefetch, 'authors').all()
                )
        return render(request, 'detail_book.html', {'book': book[0]})


class AddBook(View):
    def get(self, request):
        context = {'form': AddBookForm()}
        return render(request, 'add_book.html', context)

    def post(self, request):
        if request.user.is_authenticated:
            book_form = AddBookForm(request.POST)
            if book_form.is_valid():
                book: Book = book_form.save()
                book.authors.add(request.user)
            return redirect('detail_book', book_id=book.id)
        return redirect('list_view')


def delete_book(request, book_id):
    user = request.user
    if user.is_authenticated:
        book = Book.objects.get(id=book_id)
        if request.user in book.authors.all():
            book.delete()
            return redirect('list_view')


class UpdateBook(View):

    def get(self, request, book_id):
        book = Book.objects.get(id=book_id)
        context = {'form': AddBookForm(instance=book),
                   'book': book}
        return render(request, 'update_book.html', context)

    def post(self, request, book_id):
        user = request.user
        book = Book.objects.get(id=book_id)
        if user.is_authenticated and user in book.authors.all():
            book_form = AddBookForm(instance=book, data=request.POST)
            book_form.save()
            return redirect('detail_book', book_id=book.id)


class Login(View):
    def get(self, request):
        context = {'form': AuthenticationForm()}
        return render(request, 'login.html', context)

    def post(self, request):
        form_login = AuthenticationForm(data=request.POST)
        if form_login.is_valid():
            login(request, form_login.get_user())
            return redirect('list_view')


def logout_func(request):
    logout(request)
    return redirect('list_view')


class Register(View):

    def get(self, request):
        context = {'form': UserCreationForm()}
        return render(request, 'register.html', context)

    def post(self, request):
        rf = UserCreationForm(data=request.POST)
        if rf.is_valid():
            rf.save()
            return redirect('login')
        messages.error(request, rf.errors)
        return redirect('register')