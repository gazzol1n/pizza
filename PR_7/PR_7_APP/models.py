from django.db import models

# Модель для хранения информации о человеке
class Person(models.Model):
    name = models.CharField(max_length=100, help_text="Введите имя человека", verbose_name="Имя")
    age = models.PositiveIntegerField(help_text="Введите возраст человека", verbose_name="Возраст")

    def __str__(self):
        return f"{self.name}, {self.age} лет"

# Модель для хранения категорий
class Category(models.Model):
    name = models.CharField(max_length=100, help_text="Введите категорию", verbose_name="Категория")

    def __str__(self):
        return self.name

# Модель для хранения блюд
class Dish(models.Model):
    name = models.CharField(max_length=100, help_text="Введите название блюда", verbose_name="Название блюда")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, help_text="Выберите категорию", verbose_name="Категория")
    description = models.TextField(help_text="Введите описание блюда", verbose_name="Описание", blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, help_text="Введите цену блюда", verbose_name="Цена")

    def __str__(self):
        return f"{self.name} ({self.category.name})"
