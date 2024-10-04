import http

from django.shortcuts import render, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Iphone, SmartShop
from .serializer import IphoneSerializer, IphoneValidateSerializer
from rest_framework.exceptions import ValidationError

@api_view(['GET', 'PUT', 'DELETE'])
def iphone_detail_api_view(request, id):
    try:
        iphone = Iphone.objects.get(id=id)
        print(iphone)
    except Iphone.DoesNotExist:
        data = {
            'error': "Not found"
        }
        return Response(data=data, status=status.HTTP_404_NOT_FOUND)
    if request.method == "GET":
        data = IphoneSerializer(iphone, many=False).data
        print(data)
        return Response(data=data, status=status.HTTP_200_OK)
    elif request.method == "PUT":
        serializer = IphoneValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        iphone.name = serializer.validated_data.get('name')
        iphone.price = serializer.validated_data.get('price')
        iphone.harakter = serializer.validated_data.get('harakter')
        iphone.smart_shop = serializer.validated_data.get('smart_shop')

        return Response(status=status.HTTP_201_CREATED, data=IphoneSerializer(iphone).data)
    elif request.method == "DELETE":
        iphone.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(http_method_names=['GET', 'POST'])
def iphone_list_api_view(request):
    if request.method == 'GET':
        # 1 step база данныхтан маалыматты алуу
        iphones = Iphone.objects.all()
        # 2 step serializer json тибине откоробуз
        data = IphoneSerializer(iphones, many=True)
        print(data)
        # 3 step response аркылуу фронтко данныйды жиберуу
        return Response(data=data.data, status=200)
    elif request.method == 'POST':
        serializer = IphoneValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
        name = serializer.validated_data.get('name')
        price = serializer.validated_data.get('price')
        harakter = serializer.validated_data.get('harakter')
        smart_shop_id = serializer.validated_data.get('smart_shop')
        smart_shop = SmartShop.objects.get(id=smart_shop_id)

        iphones = Iphone.objects.create(
            name=name,
            price=price,
            harakter=harakter,
            smart_shop=smart_shop
        )


        return Response(status=status.HTTP_201_CREATED, data={"iphones_id": iphones.id})




def index(request):
    if request.method == 'GET':
        return HttpResponse("Hello, Django!")

