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


class IphoneValidateSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, max_length=24, min_length=5)
    price = serializers.IntegerField()
    harakter = serializers.CharField(required=False)
    smart_shop = serializers.IntegerField()

    # 2 ден көп болгон форманы бир убакта текшерген учурда колдонобуз.
    # def validate(self, attrs):
    #     id = attrs.get('smart_shop')
    #     try:
    #         SmartShop.objects.get(id=id)
    #     except SmartShop.DoesNotExist:
    #         raise serializers.ValidationError(f'Smart shop id {id} not found')
    #     return attrs


    # 1 гана форманы текшерген учурда колдонобуз.
    def validate_smart_shop(self, smart_shop):
        try:
            SmartShop.objects.get(id=smart_shop)
        except SmartShop.DoesNotExist:
            raise serializers.ValidationError(f'Smart shop id {smart_shop} not found')
        return smart_shop

