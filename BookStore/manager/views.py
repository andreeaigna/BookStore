from rest_framework import viewsets

from manager.serializers import BookSerializer, AuthorSerializer
from manager.models import Book, Author
from manager.constants import BookState
from rest_framework.response import Response
from rest_framework.decorators import action


# Instead of having two views for working with Tasks, we can have only one, a
# smart one
# This view can deal with all the responsibilities of the prior two views, combined
class BookViewSet(viewsets.ModelViewSet):

    serializer_class = BookSerializer
    queryset = Book.objects.all()

    @action(detail=False, methods=['GET'])
    def available_books(self, request):
        queryset = Book.objects.filter(state=BookState.AVAILABLE)
        serializer = BookSerializer(queryset, many = True)

        return Response(serializer.data)

    def filter_queryset(self, queryset):
        book=self.request.GET.get('book')
        if book:
            queryset = queryset.filter(book_id=book)

            return queryset



class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
# Create your views here.
