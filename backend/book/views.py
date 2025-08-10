from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializer
from django.http import Http404
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
# from rest_framework.viewsets import ReadOnlyModelViewSet

class BookView(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'pk'

    @action(detail=True, methods=['GET'])
    def authors(self, request, pk=None):
        book = self.get_object()
        return Response({"author": book.author})
    



# Provides list and retrieve methods only
# class BookView(ReadOnlyModelViewSet):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     lookup_field = 'pk'