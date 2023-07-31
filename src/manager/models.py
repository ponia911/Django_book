from django.db import models

class Book(models.Model):
    class Meta:
        verbose_name = 'книга'
        verbose_name_plular = 'книга'

    title = models.CharField
