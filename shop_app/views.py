from shop_app.permissions import IsLoggedInUser, NON
from shop_app.serializers import BookSerializer, OrderSerializer
from shop_app.serializers import UserSerializer
from .models import Book, User, Order
from rest_framework import viewsets
from rest_framework.permissions import AllowAny


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_permissions(self):
        return [permission() for permission in [AllowAny]]


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
