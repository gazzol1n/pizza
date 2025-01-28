"""
URL configuration for PIZZA project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from PIZZA_APP import views
from PIZZA_APP.views import login_view, register_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name="home"),
    path('logout/', views.logout_view, name='logout'),
    path('login/', login_view, name='login'),
    path('reg/', register_view, name='register'),
    path("product/", views.product, name="product"),
    path('api/cart/', views.cart_view, name='cart_view'),
    path('api/cart/update/<int:item_id>/', views.update_cart, name='update_cart'),
    path('api/cart/add/', views.add_to_cart, name='add_to_cart'),
]
