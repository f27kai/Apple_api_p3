from rest_framework import serializers
from .models import Iphone

class IphoneSerializer(serializers.ModelSerializer):

    class Meta:
        model = Iphone
        fields = '__all__'