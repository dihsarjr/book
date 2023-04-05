from django.urls import path
from book_api.views import get_book_list

urlpatterns = [
    path('list/', get_book_list),
]