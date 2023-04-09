from django.urls import path
from book_api.views import BookList,BookCreate,BookDetails

urlpatterns = [
    # path('list/', get_book_list),
    # path('',book_create),
    # path('<int:pk>',book)
    path('list/',BookList.as_view()),
    path('',BookCreate.as_view()),
    path('<int:pk>',BookDetails.as_view())
]