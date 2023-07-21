from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def home_page(request):
    return render(request, 'library/home.html')


def add_book(request):
    return render(request, 'library/add_book.html')