from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from .models import Cart, CartItem, Dish, Category
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
import json
from rest_framework import viewsets, permissions
from .models import Category, Dish, Cart, CartItem
from .serializers import CategorySerializer, DishSerializer, CartSerializer, CartItemSerializer
from django.contrib.auth.models import User
from .serializers import UserSerializer
import pandas as pd
from django.shortcuts import render, redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from .forms import ExcelUploadForm
from .models import Category, Dish


def home(request):
    categories = Category.objects.prefetch_related('dish_set')
    return render(request, "HOME/index.html", {'categories': categories})



def product(request):
    return render(request, "PRODUCT/index.html")

def logout_view(request):
    logout(request)  # Завершаем сессию пользователя
    return redirect('home')  # Перенаправляем на страницу входа (или на любую другую)


def cart_view(request):
    cart, _ = Cart.objects.get_or_create(customer=request.user)
    items = [
        {
            'id': item.id,
            'dish': {
                'name': item.dish.name,
                'price': float(item.dish.price),
                'image_url': item.dish.image.url,
            },
            'quantity': item.quantity,
        }
        for item in cart.items.all()
    ]
    return JsonResponse({'items': items})

@csrf_exempt
def update_cart(request, item_id):
    cart, _ = Cart.objects.get_or_create(customer=request.user)
    cart_item = CartItem.objects.get(id=item_id, cart=cart)

    data = json.loads(request.body)
    delta = data.get('delta', 0)

    cart_item.quantity += delta
    if cart_item.quantity <= 0:
        cart_item.delete()
    else:
        cart_item.save()

    return JsonResponse({'message': 'Cart updated successfully'})


@csrf_exempt
def add_to_cart(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        dish_id = data.get('dish_id')
        dish = Dish.objects.get(id=dish_id)
        
        cart, _ = Cart.objects.get_or_create(customer=request.user)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, dish=dish)
        if not created:
            cart_item.quantity += 1
        cart_item.save()
        
        return JsonResponse({'message': f'{dish.name} добавлен в корзину!'})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')  # Перенаправление на главную страницу, если пользователь уже авторизован

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)  # Создаём форму аутентификации
        if form.is_valid():
            user = form.get_user()  # Получаем пользователя из формы
            login(request, user)  # Авторизуем пользователя
            return redirect('home')
        else:
            messages.error(request, 'Неверные логин или пароль!')

    else:
        form = AuthenticationForm()  # Пустая форма

    return render(request, 'LOGIN/index.html', {'form': form})


def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')  # Перенаправление на главную страницу, если пользователь уже авторизован

    if request.method == 'POST':
        form = UserCreationForm(request.POST)  # Создаём форму регистрации
        if form.is_valid():
            user = form.save()  # Сохраняем нового пользователя
            login(request, user)  # Авторизуем пользователя
            messages.success(request, 'Регистрация прошла успешно!')
            return redirect('home')  # Перенаправление на главную страницу
        else:
            messages.error(request, 'Ошибка регистрации. Проверьте введенные данные.')

    else:
        form = UserCreationForm()  # Пустая форма

    return render(request, 'LOGIN/reg.html', {'form': form})


#Excel - Импорт из таблицы
@staff_member_required
def import_excel(request):
    if request.method == 'POST':
        form = ExcelUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            model_choice = form.cleaned_data['model_choice']
            df = pd.read_excel(file)

            if model_choice == 'category':
                for _, row in df.iterrows():
                    print("1")
                    Category.objects.get_or_create(name=row['name'])
            elif model_choice == 'dish':
                print("2")
                for _, row in df.iterrows():
                    category, _ = Category.objects.get_or_create(name=row['category'])
                    Dish.objects.create(
                        name=row['name'],
                        price=row['price'],
                        image=row['image'],
                        dis=row['dis'],
                    ).type.add(category)

            messages.success(request, "Данные успешно импортированы!")
            return redirect('import_excel')
    
    else:
        form = ExcelUploadForm()

    return render(request, 'import_excel.html', {'form': form})



#API

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]  #---<Без токенов доступа>---# 

class DishViewSet(viewsets.ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    permission_classes = [permissions.AllowAny]  #---<Без токенов доступа>---# 

class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [permissions.AllowAny]  #---<Без токенов доступа>---# 

class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [permissions.AllowAny]  #---<Без токенов доступа>---# 

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]  #---<Без токенов доступа>---#
