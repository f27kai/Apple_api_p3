from django.urls import path
from .views import (
    registration_api_view,
    Authorization_api_view
)



urlpatterns = [
    path('registration/', registration_api_view, name='reqistration'),
    path('authorization/', Authorization_api_view.as_view(), name='authorization')
]