from django.contrib import admin
from .models import Category, Ingredient, PizzaSize, DoughType, Pizza, Order

admin.site.register(Category)
admin.site.register(Ingredient)
admin.site.register(PizzaSize)
admin.site.register(DoughType)
admin.site.register(Pizza)
admin.site.register(Order)
