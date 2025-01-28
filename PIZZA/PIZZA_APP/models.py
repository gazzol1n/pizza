from django.db import models
from django.contrib.auth.models import User  # Если используешь встроенную модель пользователя

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Dish(models.Model):  # Модель блюда
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.FileField(upload_to="static/IMG/PRODUCT", default="static/IMG/PRODUCT/PIZZA.png")
    dis = models.TextField(default="pizza")
    type = models.ManyToManyField(Category)

    def __str__(self):
        return self.name


class Cart(models.Model):  # Модель корзины
    customer = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cart')
    created_at = models.DateTimeField(auto_now_add=True)

    def get_total_price(self):
        """Считает общую цену корзины"""
        return sum(item.get_total_price() for item in self.items.all())

    def __str__(self):
        return f"Cart of {self.customer.username}"

class CartItem(models.Model):  # Позиция в корзине
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def get_total_price(self):
        """Считает цену позиции"""
        return self.dish.price * self.quantity

    def __str__(self):
        return f"{self.dish.name} x {self.quantity}"
