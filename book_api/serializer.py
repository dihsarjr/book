# from rest_framework import serializers
# from book_api.models import Book


# class BookSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField()
#     number_of_page = serializers.IntegerField()
#     published_date = serializers.DateField()
#     quantity = serializers.IntegerField()

#     def create(self, data):
#         return Book.objects.create(**data)

#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.number_of_page = validated_data.get(
#             'number_of_page', instance.number_of_page)
#         instance.published_date = validated_data.get(
#             'published_date', instance.published_date)
#         instance.quantity = validated_data.get('quantity', instance.quantity)

#         instance.save()
#         return instance


from rest_framework import serializers
from book_api.models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta():
        model = Book
        fields = '__all__'