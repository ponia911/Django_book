from django.urls import path
from manager.views import *




urlpatterns = [
    path('456/', BookView.as_view())

]