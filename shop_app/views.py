from django.http import HttpResponse, JsonResponse, Http404

from shop_app.permissions import IsLoggedInUser, NON
from shop_app.serializers import BookSerializer

from shop_app.serializers import UserSerializer
from .models import Book, User
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, NOT
from rest_auth.registration.views import RegisterView
from rest_framework.decorators import action
from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404


class BookViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_permissions(self):
        return [permission() for permission in [AllowAny]]

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [AllowAny]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsLoggedInUser]
        elif self.action == 'list':
            permission_classes = [NON]
        return [permission() for permission in permission_classes]
