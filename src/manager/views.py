from django.shortcuts import render
from django.views import View

from manager.models import Book


class BookView(View):
    def get(self, request):
        data = {'books': Book.objects.all()}
        return render(request, 'index.html', context= data)
