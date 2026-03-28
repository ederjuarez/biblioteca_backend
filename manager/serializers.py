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
    author_name = serializers.SerializerMethodField()

    def get_author_name(self, obj):
        # We handle case if author is not there to prevent errors in some edge cases
        return obj.author.name if obj.author else None

    class Meta:
        model = Book
        fields = "__all__"
