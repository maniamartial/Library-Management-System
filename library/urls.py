from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('add_book', views.add_book, name='add_book')
]