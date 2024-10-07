from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import UserRegistrationSerializer, UserAuthenticationSerializer



@api_view(['POST'])
def registration_api_view(request):
    serializer = UserRegistrationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    username = serializer.validated_data.get('username')
    password = serializer.validated_data.get('password')

    User.objects.create_user(username=username, password=password)

    return Response(status=status.HTTP_200_OK)

@api_view(['POST'])
def authorization_api_view(request):
    serializer = UserAuthenticationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    username = serializer.validated_data.get('username')
    password = serializer.validated_data.get('password')

    user = authenticate(username=username, password=password)
    print(user)
    if user:
        token, _ = Token.objects.get_or_create(user=user)
        return Response(status=status.HTTP_200_OK, data={'key': token.key})
    return Response(status=status.HTTP_404_NOT_FOUND, data={'This is user not authorized'})
