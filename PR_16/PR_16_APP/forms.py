from django import forms
from .models import Person

class UserForm(forms.ModelForm): 
    class Meta: 
        model = Person  # связанная модель
        fields = ['name', 'age', "image"]  # поля формы
