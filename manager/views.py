from django.shortcuts import render
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import filters
from .pagination import CustomPagination
from django_filters.rest_framework import DjangoFilterBackend

class AuthorViewSet(viewsets.ModelViewSet):   
    serializer_class = AuthorSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

    def get_queryset(self):
        queryset = Author.objects.all().order_by("-pk")
        return queryset

    @action(detail=False, methods=["get"])
    def list_filter(self, request):
        queryset = self.get_queryset().filter(birth_date__year__gte=1950)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by("pk")
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['author_id']
