from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Genre, Book
from .serializers import GenreSerializer, BookSerializer

class GenreAPIView(APIView):
    def get(self, request):
        janrlar = Genre.objects.all()
        seralizer = GenreSerializer(janrlar, many=True)
        return Response(seralizer.data)

    def post(self, request):
        seralizer = GenreSerializer(data=request.data)
        if seralizer.is_valid():
            seralizer.save()
            return Response(seralizer.data)
        return Response(seralizer.errors)

class BookAPIView(APIView):
    def get(self, request):
        kitoblar = Book.objects.all()
        seralizer = BookSerializer(kitoblar, many=True)
        return Response(seralizer.data)

    def post(self, request):
        seralizer = BookSerializer(data=request.data)
        if seralizer.is_valid():
            seralizer.save()
            return Response(seralizer.data)
        return Response(seralizer.errors)
