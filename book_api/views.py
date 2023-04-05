from django.shortcuts import render
from book_api.models import Book
from django.http import JsonResponse

# Create your views here.

def get_book_list():
    book_list = Book.objects.all()
    bool_python = list(book_list.values)
    return JsonResponse({
        'book_list' : book_list,
    })

