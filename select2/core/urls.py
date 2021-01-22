from django.urls import path
from .views import *

urlpatterns = [
    path('AAA', inicio, name='index')
]