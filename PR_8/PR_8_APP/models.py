from django.db import models
from django.urls import reverse

# Модель для хранения категорий пиццы (например, мясная, вегетарианская)
class Category(models.Model):
    name = models.CharField(max_length=200, help_text="Введите категорию пиццы", verbose_name="Категория пиццы")

    def __str__(self):
        return self.name

# Модель для хранения ингредиентов пиццы
class Ingredient(models.Model):
    name = models.CharField(max_length=100, help_text="Введите название ингредиента", verbose_name="Ингредиент")
    is_vegetarian = models.BooleanField(default=False, help_text="Этот ингредиент вегетарианский?", verbose_name="Вегетарианский")

    def __str__(self):
        return self.name

# Модель для хранения информации о размерах пиццы
class PizzaSize(models.Model):
    size = models.CharField(max_length=20, help_text="Введите размер пиццы", verbose_name="Размер пиццы")
    diameter = models.IntegerField(help_text="Введите диаметр пиццы в см", verbose_name="Диаметр (см)")

    def __str__(self):
        return f"{self.size} ({self.diameter} см)"

# Модель для хранения информации о типах теста для пиццы
class DoughType(models.Model):
    name = models.CharField(max_length=50, help_text="Введите тип теста", verbose_name="Тип теста")

    def __str__(self):
        return self.name

# Модель для хранения пицц
class Pizza(models.Model):
    name = models.CharField(max_length=200, help_text="Введите название пиццы", verbose_name="Название пиццы")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, help_text="Выберите категорию пиццы", verbose_name="Категория")
    ingredients = models.ManyToManyField(Ingredient, help_text="Выберите ингредиенты для пиццы", verbose_name="Ингредиенты")
    size = models.ForeignKey(PizzaSize, on_delete=models.CASCADE, help_text="Выберите размер пиццы", verbose_name="Размер пиццы")
    dough_type = models.ForeignKey(DoughType, on_delete=models.CASCADE, help_text="Выберите тип теста", verbose_name="Тип теста")
    price = models.DecimalField(max_digits=6, decimal_places=2, help_text="Введите цену пиццы", verbose_name="Цена")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('pizza-detail', args=[str(self.id)])

# Модель для хранения заказов на пиццу
class Order(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE, help_text="Выберите пиццу", verbose_name="Пицца")
    quantity = models.PositiveIntegerField(help_text="Введите количество", verbose_name="Количество")
    customer_name = models.CharField(max_length=100, help_text="Введите имя клиента", verbose_name="Имя клиента")
    address = models.CharField(max_length=200, help_text="Введите адрес доставки", verbose_name="Адрес доставки")
    phone_number = models.CharField(max_length=15, help_text="Введите номер телефона клиента", verbose_name="Номер телефона")
    order_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата заказа")
    status = models.CharField(max_length=20, default="Принят", help_text="Статус заказа", verbose_name="Статус заказа")

    def __str__(self):
        return f"Заказ {self.id} - {self.pizza.name} x {self.quantity}"
