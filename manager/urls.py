from django.urls import path
from .views import AuthorViewSet, BookViewSet

urlpatterns = [
    path("authors/", AuthorViewSet.as_view({"get": "list", "post": "create"}), name="author-list"),
    path("authors/<int:pk>/", AuthorViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"}), name="author-detail"),
    path("list_filter/", AuthorViewSet.as_view({"get": "list_filter"}), name="author-list-2"),
    path("books/", BookViewSet.as_view({"get": "list", "post": "create"}), name="book-list"),
    path("books/<int:pk>/", BookViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy", "patch": "partial_update"}), name="book-detail"),
    path("books_author/<int:author_id>/", BookViewSet.as_view({"get": "books_author"}), name="book-author"),
]
