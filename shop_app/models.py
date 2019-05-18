from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.conf import settings


class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    author = models.CharField(max_length=255)
    bookName = models.CharField(max_length=255)
    price = models.IntegerField()
    image = models.CharField(max_length=255)


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    username = models.CharField(blank=True, null=True, max_length=255)
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', ]

    def __str__(self):
        return "{}".format(self.email)


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    dob = models.DateField()
    address = models.CharField(max_length=255)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zip = models.CharField(max_length=5)

# class User(models.Model):
#   id = models.UUIDField(primary_key=True, default=uuid.uuid4())
#  name = models.CharField(max_length=50)
# last_name = models.CharField(max_length=50)
# patronymic = models.CharField(max_length=50)
# address = models.CharField(max_length=500)
# password = models.CharField(max_length=100)
# Create your models here.
