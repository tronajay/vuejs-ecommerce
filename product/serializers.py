from rest_framework import serializers
from .models import Product, ProductCategory
from base.services import slugify

class ProductCategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    uuid = serializers.UUIDField(read_only=True)
    name = serializers.CharField(max_length=100)
    image_url = serializers.URLField(max_length=100,required=False,allow_null=True)

    def validate(self,attrs):
        if "name" in attrs.keys():
            name = attrs.get('name')
            attrs["slug"] = slugify(name)
        return attrs

    def create(self,validated_data):
        return ProductCategory.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        for key in validated_data.keys():
            setattr(instance, key, validated_data[key])
        instance.save()
        return instance

class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    uuid = serializers.UUIDField(read_only=True)
    slug = serializers.SlugField(read_only=True)
    name = serializers.CharField(max_length=100)
    desc = serializers.CharField(max_length=1000)
    price = serializers.CharField(max_length=20)
    selling_price = serializers.CharField(max_length=20)
    feature_img = serializers.URLField(max_length=500)

    def validate(self, attrs):
        if "name" in attrs.keys():
            name = attrs.get('name')
            attrs["slug"] = slugify(name)
        return attrs

    def create(self,validated_data):
        return Product.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        for key in validated_data.keys():
            setattr(instance, key, validated_data[key])
        instance.save()
        return instance