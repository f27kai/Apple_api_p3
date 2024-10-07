from django.urls import path
from .views import (
    registration_api_view,
    authorization_api_view
)



urlpatterns = [
    path('registration/', registration_api_view, name='reqistration'),
    path('authorization/', authorization_api_view, name='authorization')
]