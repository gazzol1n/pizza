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


