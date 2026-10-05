from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Genre, Book

class GenreAPIView(APIView):
    def get(self, request):
        janrlar = Genre.objects.all()
        data = [{'id': j.id, 'name': j.name} for j in janrlar]
        return Response(data)

    def post(self, request):
        name = request.data.get('name')
        janr = Genre.objects.create(name=name)
        return Response({'id': janr.id, 'name': janr.name})

class BookAPIView(APIView):
    def get(self, request):
        kitoblar = Book.objects.all()
        data = [{'id': k.id, 'title': k.title, 'price': str(k.price), 'genre_id': k.genre_id} for k in kitoblar]
        return Response(data)

    def post(self, request):
        title = request.data.get('title')
        price = request.data.get('price')
        genre_id = request.data.get('genre_id')
        kitob = Book.objects.create(title=title, price=price, genre_id=genre_id)
        return Response({
            'id': kitob.id, 
            'title': kitob.title, 
            'price': str(kitob.price), 
            'genre_id': kitob.genre_id
        })
