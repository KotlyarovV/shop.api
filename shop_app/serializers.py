from django.contrib.auth.models import User
from rest_framework import serializers
from shop_app.models import Book, UserProfile, User, Order, BookInOrder


class BookInOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookInOrder
        fields = ('book', 'quantity')


class OrderSerializer(serializers.ModelSerializer):
    order = BookInOrderSerializer(many=True)

    class Meta:
        model = Order
        fields = ('address', 'country', 'city', 'zip', 'order', 'email')

    def create(self, validated_data):
        books_in_order_data = validated_data.pop('order')
        order = Order.objects.create(**validated_data)
        for book_data in books_in_order_data:
            BookInOrder.objects.create(order=order, **book_data)

        request = self.context.get("request")
        if request and hasattr(request, "user"):
            order.user = request.user

        return order


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('dob', 'address', 'country', 'city', 'zip')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    profile = UserProfileSerializer(required=True)

    class Meta:
        model = User
        fields = ('url', 'email', 'first_name', 'last_name', 'password', 'profile')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        UserProfile.objects.create(user=user, **profile_data)
        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        profile = instance.profile

        instance.email = validated_data.get('email', instance.email)
        instance.save()

        profile.dob = profile_data.get('dob', profile.dob)
        profile.address = profile_data.get('address', profile.address)
        profile.country = profile_data.get('country', profile.country)
        profile.city = profile_data.get('city', profile.city)
        profile.zip = profile_data.get('zip', profile.zip)
        profile.save()

        return instance


class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'author', 'bookName', 'price', 'image')
