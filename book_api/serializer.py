from rest_framework import serializers
from book_api.models import Book

class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    number_of_page = serializers.IntegerField()
    published_date= serializers.DateField()
    quantity = serializers.IntegerField()

    def create(self, data):
        return Book.objects.create(**data)

