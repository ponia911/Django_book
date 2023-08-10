from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.db.models import Count

from manager.models import Book



class Command(BaseCommand):



    def handle(self, *args, **options):
        Books = Book.objects.annotate(likes_book=Count('likes'))
        for book in Books:
            book.count_likes = book.likes_book
            print(book.count_likes)
            Book.objects.bulk_update(Books, ['count_likes'], batch_size=1000)
