import http

from django.shortcuts import render, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Iphone
from .serializer import IphoneSerializer


@api_view(['GET'])
def iphone_detail_api_view(request, id):
    try:
        iphone = Iphone.objects.get(id=id)
        print(iphone)
    except Iphone.DoesNotExist:
        data = {
            'error': "Not found"
        }
        return Response(data=data, status=status.HTTP_404_NOT_FOUND)
    data = IphoneSerializer(iphone, many=False).data
    print(data)
    return Response(data=data, status=status.HTTP_200_OK)

@api_view(http_method_names=['GET'])
def iphone_list_api_view(request):
    # 1 step база данныхтан маалыматты алуу
    iphones = Iphone.objects.all()
    # 2 step serializer json тибине откоробуз
    data = IphoneSerializer(iphones, many=True)
    print(data)
    # 3 step response аркылуу фронтко данныйды жиберуу
    return Response(data=data.data, status=200)



def index(request):
    if request.method == 'GET':
        return HttpResponse("Hello, Django!")
