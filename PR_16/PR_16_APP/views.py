from .forms import UserForm 
from django.shortcuts import render, redirect 
from .models import Person 
import os
from PR_16 import settings
 
def index(request): 
    my_text = 'Изучаем модели Django'     
    people_kol = Person.objects.count()     
    context = {'my_text': my_text, "people_kol": people_kol}     
    return render(request, "firstapp/index.html", context) 
 
def about(request): 
    return render(request, "firstapp/about.html") 
 
def contact(request): 
    return render(request, "firstapp/contact.html") 
 
# взаимодействие с формой ввода данных о клиентах 
def my_form(request):     
    if request.method == "POST":  # пользователь отправил данные         
        form = UserForm(request.POST)  # создание экземпляра формы 
        if form.is_valid():  # проверка валидности формы             
            form.save()  # запись данных в БД 
            # остаемся на той же странице, обновляем форму 
 
    # Загрузить форму для ввода клиентов     
    my_text = 'Сведения о клиентах'     
    people = Person.objects.all()     
    form = UserForm()     
    context = {'my_text': my_text, "people": people, "form": form}     
    return render(request, "firstapp/my_form.html", context) 


def edit_form(request, id): 
    person = Person.objects.get(id=id)    
    if request.method == "POST":        
        print(request.POST)
        person.name = request.POST.get("name")         
        person.age = request.POST.get("age")
        if "image" in request.FILES:
                image_file = request.FILES["image"]
                static_path = os.path.join(settings.BASE_DIR, "static/")
                
                # Создаем папку, если она не существует
                os.makedirs(static_path, exist_ok=True)

                # Генерируем путь для сохранения файла
                file_path = os.path.join(static_path, image_file.name)
                
                # Сохраняем файл
                with open(file_path, "wb+") as destination:
                    for chunk in image_file.chunks():
                        destination.write(chunk)
                
                # Обновляем путь к изображению в модели
                person.image = f"{image_file.name}"

        person.save() 
        return redirect('my_form') 
        
    data = {"person": person} 
    return render(request, "firstapp/edit_form.html", context=data) 

def del_form(request, id): 
    person = Person.objects.get(id=id)    
    person.delete() 
    return redirect('my_form') 

