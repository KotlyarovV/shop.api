from django.http import HttpResponse, JsonResponse, Http404

from shop_app.serializers import BookSerializer

from shop_app.serializers import UserSerializer
from .models import Book, User
from rest_framework import viewsets
from rest_auth.registration.views import RegisterView
from rest_framework.decorators import action
from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
#def index(request):
 #   books = Book.objects.values()
  #  return JsonResponse({"books" : list(books)}, safe=False)

#def detail(request, book_id):
 #   book = get_object_or_404(Book, id=book_id)
  #  return JsonResponse(model_to_dict(book))
    #try:
     #   book = Book.objects.get(id=book_id)
      #  return JsonResponse(model_to_dict(book))
    #except Book.DoesNotExist:
     #   return Http404()

