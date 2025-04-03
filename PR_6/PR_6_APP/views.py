from django.shortcuts import render

def index(request):
    return render(request, "MyPizza\index.html")

def login(request):
    return render(request, "Login\index.html")

def cart(request):
    return render(request, "Cart\index.html")
