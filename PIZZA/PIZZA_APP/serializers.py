from rest_framework import serializers
from .models import Category, Dish, Cart, CartItem
from django.contrib.auth.models import User
import requests
from django.core.files.base import ContentFile

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class DishSerializer(serializers.ModelSerializer):
    image_url = serializers.URLField(write_only=True, required=False)
    type = serializers.ListField(child=serializers.IntegerField(), write_only=True)  # Ожидаем список ID категорий
    type_display = CategorySerializer(many=True, read_only=True)  # Отображение категорий

    class Meta:
        model = Dish
        fields = ['id', 'name', 'price', 'image', 'image_url', 'dis', 'type', 'type_display']

    def create(self, validated_data):
        image_url = validated_data.pop('image_url', None)
        type_ids = validated_data.pop('type', [])  # Забираем список категорий
        
        dish = Dish.objects.create(**validated_data)  # Создаём объект без категорий
        if type_ids:
            dish.type.set(type_ids)  # Устанавливаем категории через .set()
        
        if image_url:
            response = requests.get(image_url)
            if response.status_code == 200:
                dish.image.save(f"{dish.name}.jpg", ContentFile(response.content), save=True)
        
        return dish

    def update(self, instance, validated_data):
        type_ids = validated_data.pop('type', None)
        if type_ids is not None:
            instance.type.set(type_ids)  # Обновляем ManyToManyField

        return super().update(instance, validated_data)


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
