from django.shortcuts import render
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


class AuthorViewSet(viewsets.ModelViewSet):
    # pagination_class = None
    # permission_classes = [AllowAny]
    # queryset = Author.objects.all().order_by("-pk")
    serializer_class = AuthorSerializer

    def get_queryset(self):
        data_filer = self.request.query_params.get("data_filer", None)
        queryset = Author.objects.all().order_by("-pk")
        for value in data_filer:
            if value == "name":
                queryset = queryset.filter(name=value)
            if value == "birth_date":
                queryset = queryset.filter(birth_date=value)
        return queryset


    @action(detail=False, methods=["get"])
    def list_filter(self, request):
        queryset = self.get_queryset().filter(birth_date__year__gte=1950)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by("pk")
    serializer_class = BookSerializer
    # permission_classes = [AllowAny]
  
    @action(detail=False, methods=["get"])
    def books_author(self, request, author_id):        
        queryset = self.get_queryset().filter(author=author_id)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
