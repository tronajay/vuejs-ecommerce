from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from .models import Address

class UserSerializer(serializers.Serializer):
    username = serializers.CharField(
        max_length=100,
        validators=[UniqueValidator(queryset=User.objects.all())],
        )
    email = serializers.EmailField(max_length=100)
    password = serializers.CharField(max_length=100,write_only=True)

    def create(self,validated_data):
        password = validated_data.pop("password")
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return validated_data

class UserAddressSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    address_1 = serializers.CharField(max_length=200)
    address_2 = serializers.CharField(max_length=200,required=False,allow_blank=True)
    city = serializers.CharField(max_length=100)
    state = serializers.CharField(max_length=50)
    postal_code = serializers.CharField(max_length=6)
    phone = serializers.CharField(max_length=13)
    company = serializers.CharField(required=False,max_length=50)

    def create(self, validated_data):
        return Address.objects.create(**validated_data)