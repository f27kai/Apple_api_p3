from rest_framework import serializers
from .models import Iphone, SmartShop

class SmartShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = SmartShop
        fields = 'name year age_shop'.split()


class IphoneSerializer(serializers.ModelSerializer):
    smart_shop = SmartShopSerializer(many=False)
    class Meta:
        model = Iphone
        fields = '__all__'
        # depth = 1