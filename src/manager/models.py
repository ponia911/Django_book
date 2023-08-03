from django.db import models

class Book(models.Model):
    class Meta:
        verbose_name = 'книга'
        verbose_name_plular = 'книги'

    title = models.CharField(max_length=100, verbose_name='название книги')
