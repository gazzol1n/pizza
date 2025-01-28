from django.db import models

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
