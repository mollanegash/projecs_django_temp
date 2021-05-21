
from django.urls import path
from .import views
urlspatters = [
path('', views.home, name = 'home')

]