from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField(max_length=100)
    desc = serializers.CharField(max_length=1000)
    price = serializers.CharField(max_length=20)
    selling_price = serializers.CharField(max_length=20)
    feature_img = serializers.URLField(max_length=500)

    def create(self,validated_data):
        return Product.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        for key in validated_data.keys():
            setattr(instance, key, validated_data[key])
        instance.save()
        return instance