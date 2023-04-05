from rest_framework import serializers

class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    number_of_page = serializers.IntegerField()
    published_date= serializers.DateFieldJ()
    quantity = serializers.IntegerFieldJ()

