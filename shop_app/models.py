from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    username = models.CharField(blank=True, null=True, max_length=255)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username']

    def __str__(self):
        return "{}".format(self.email)


class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    address = models.CharField(max_length=255)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zip = models.CharField(max_length=5)
    is_payed = models.BooleanField(default=False)
    email = models.CharField(max_length=100, default=None, null=True)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)


class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    author = models.CharField(max_length=255)
    bookName = models.CharField(max_length=255)
    price = models.IntegerField()
    image = models.CharField(max_length=255)


class BookInOrder(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    order = models.ForeignKey(Order, related_name='order', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    dob = models.DateField()
    address = models.CharField(max_length=255)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zip = models.CharField(max_length=5)
