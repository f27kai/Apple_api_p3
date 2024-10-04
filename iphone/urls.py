from django.urls import path
from .views import (
    index,
    iphone_list_api_view,
    iphone_detail_api_view
)

urlpatterns = [
    path('index/', index, name='index'),
    path('iphone_list/', iphone_list_api_view, name='iphone_list'), # GET <-> POST
    path('iphone_detail/<int:id>/', iphone_detail_api_view, name='iphone_detail') # GET <-> PUT <-> DELETE
]