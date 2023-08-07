from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

from manager.models import Book


class Command(BaseCommand):
    help = 'add simple data to db'


def handle(self, *args, **options):
    Book.objects.all().delete()
    User.objects.create(username="Boris")
