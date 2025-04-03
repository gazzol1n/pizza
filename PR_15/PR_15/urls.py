from django.contrib import admin
from django.urls import path
from PR_15_APP import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('form/', views.my_form, name='my_form'),
]
