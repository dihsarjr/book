from django.shortcuts import render
from book_api.models import Book
from django.http import JsonResponse
from book_api.serializer import BookSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET'])
def get_book_list(request):
    book_list = Book.objects.all()
    serializer = BookSerializer(book_list,many = True)
    return Response(serializer.data)


