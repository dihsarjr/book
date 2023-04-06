from django.urls import path
from book_api.views import get_book_list,book_create,book

urlpatterns = [
    path('list/', get_book_list),
    path('',book_create),
    path('<int:pk>',book)
]