from django.db import models
from django.contrib.auth.models import User

class Capital(models.Model):
    capital_city = models.CharField(max_length=200)
    capital_population = models.IntegerField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Связь с автором (пользователем)

    def __str__(self):
        return self.capital_city
