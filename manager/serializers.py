from rest_framework import serializers
from .models import Book, Author


class AuthorSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    def get_full_name(self, obj):
        return f"{obj.name} ({obj.birth_date})"

    class Meta:
        model = Author
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):
    # author = AuthorSerializer()
    author_name = serializers.SerializerMethodField()

    def get_author_name(self, obj):
        return obj.author.name

    class Meta:
        model = Book
        fields = "__all__"
