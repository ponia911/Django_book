from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from manager.models import Book


class Command(BaseCommand):
    help = 'add simple data to db'


    def handle(self, *args, **options):
        # Book.objects.all().delete()
        users = User.objects.all()
        book1 = Book(title='book1', text='text for book 1')
        book2 = Book(title='book2', text='text for book 2')
        book3 = Book(title='book3', text='text for book 3')
        Book.objects.bulk_create([book1, book2, book3])

        for book in Book.objects.all():
            book.authors.add(users[0], users[2])
            book.save()
        #User.objects.create(username="Boris")
