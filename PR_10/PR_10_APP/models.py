from django.db import models
from django.contrib.auth.models import User
from datetime import date

class Category(models.Model):
    name = models.CharField(max_length=200, help_text="Введите категорию блюда, например, 'Пицца'")

    def __str__(self):
        return self.name

class Dish(models.Model):
    name = models.CharField(max_length=200, help_text="Введите название блюда")
    description = models.TextField(max_length=1000, help_text="Введите описание блюда")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.name} ({self.category})"

class Order(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, verbose_name="Блюдо")
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Заказчик")
    date_ordered = models.DateField(default=date.today, verbose_name="Дата заказа")

    def __str__(self):
        return f"Заказ {self.dish.name} для {self.customer.username if self.customer else 'гостя'} от {self.date_ordered}"
