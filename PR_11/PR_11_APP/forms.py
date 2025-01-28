from django import forms
from .models import Order, Category, Dish

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['dish']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        labels = {
            'name': 'Название категории',
        }

class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ['name', 'description', 'category', 'price']
        labels = {
            'name': 'Название блюда',
            'description': 'Описание',
            'category': 'Категория',
            'price': 'Цена (в рублях)',
        }