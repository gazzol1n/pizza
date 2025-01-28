from django.contrib import admin
from .models import Cart, CartItem, Dish, Category

admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Dish)
admin.site.register(Category)
