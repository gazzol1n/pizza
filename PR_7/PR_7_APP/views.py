from django.shortcuts import render, redirect, get_object_or_404
from .models import Person, Category, Dish

# Рендер главной страницы
def index(request):
    people = Person.objects.all()
    categories = Category.objects.all()
    dishes = Dish.objects.all()
    return render(request, "index.html", {"people": people, "categories": categories, "dishes": dishes})

# Создание объектов
def create_person(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        Person.objects.create(name=name, age=age)
    return redirect('index')

def create_category(request):
    if request.method == "POST":
        name = request.POST.get("name")
        Category.objects.create(name=name)
    return redirect('index')

def create_dish(request):
    if request.method == "POST":
        name = request.POST.get("name")
        category_id = request.POST.get("category_id")
        description = request.POST.get("description")
        price = request.POST.get("price")
        category = get_object_or_404(Category, id=category_id)
        Dish.objects.create(name=name, category=category, description=description, price=price)
    return redirect('index')

# Редактирование объектов
def edit_person(request, id):
    person = get_object_or_404(Person, id=id)
    if request.method == "POST":
        person.name = request.POST.get("name")
        person.age = request.POST.get("age")
        person.save()
        return redirect('index')
    return render(request, "edit_person.html", {"person": person})

def edit_category(request, id):
    category = get_object_or_404(Category, id=id)
    if request.method == "POST":
        category.name = request.POST.get("name")
        category.save()
        return redirect('index')
    return render(request, "edit_category.html", {"category": category})

def edit_dish(request, id):
    dish = get_object_or_404(Dish, id=id)
    categories = Category.objects.all()
    if request.method == "POST":
        dish.name = request.POST.get("name")
        dish.category_id = request.POST.get("category_id")
        dish.description = request.POST.get("description")
        dish.price = request.POST.get("price")
        dish.save()
        return redirect('index')
    return render(request, "edit_dish.html", {"dish": dish, "categories": categories})

# Удаление объектов
def delete_person(request, id):
    person = get_object_or_404(Person, id=id)
    person.delete()
    return redirect('index')

def delete_category(request, id):
    category = get_object_or_404(Category, id=id)
    category.delete()
    return redirect('index')

def delete_dish(request, id):
    dish = get_object_or_404(Dish, id=id)
    dish.delete()
    return redirect('index')
