from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def hello_from_signal(created, instance, **kwargs):
    if created:
        print(f'hello from signal {instance.username}')
    else:
        print(f'bye from signal {instance.username}')