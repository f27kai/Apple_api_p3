from django.urls import path
from .views import (
    index,
    iphone_list_api_view,
    iphone_detail_api_view,
    # SmartShopListCreateView,  # GET -> ListApiView, POST -> CreateApiView
    # SmartShopDetailView
    SmartShopView,
    IphonelistView
)

urlpatterns = [
    path('index/', index, name='index'),
    path('iphone_list/', iphone_list_api_view, name='iphone_list'), # GET -> ListApiView, POST -> CreateApiView
    path('iphone_detail/<int:id>/', iphone_detail_api_view, name='iphone_detail'), # GET -> retrieve, PUT -> UpdateApiView, DELETE -> destroy
    # path('smart_shop_list/', SmartShopListCreateView.as_view(), name='smart_shop_list'), # GET -> ListApiView, POST -> CreateApiView
    # path('smart_shop_detail/<int:pk>/', SmartShopDetailView.as_view(), name='smart_shop_detail'), # GET -> retrieve, PUT -> UpdateApiView, DELETE -> destroy
    path('smart_shop/', SmartShopView.as_view({
        'get': 'list',
        'post': 'create'
    }), name='smart_shop'),
    path('smart_shop/<int:pk>', SmartShopView.as_view({
        'get':'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('iphone_class/', IphonelistView.as_view(), name='iphone')
]
