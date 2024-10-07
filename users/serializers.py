from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError

class UserAuthenticationSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

class UserRegistrationSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate_username(self, username):
        if User.objects.filter(username=username).exists():
            raise ValidationError("User already exists!")
        return username
