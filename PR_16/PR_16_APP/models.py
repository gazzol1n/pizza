from django.db import models

class User(models.Model): 
    name = models.CharField(max_length=20) 
 
class Account(models.Model):     
    login = models.CharField(max_length=20)     
    password = models.CharField(max_length=20)     
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True) 


from django.db import models

class Person(models.Model):     
    name = models.CharField(max_length=20, verbose_name="Имя клиента") 
    age = models.IntegerField(verbose_name="Возраст клиента")   
    image = models.FileField(verbose_name="Изображение", default="IMG.png", upload_to="static")  

    # Не нужно явно объявлять objects, если он стандартный
    objects = models.Manager()  # это создается автоматически, можно не указывать

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

    def __str__(self):
        return self.name


