from django.contrib import admin
from django.urls import path
from PR_16_APP import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('form/', views.my_form, name='my_form'),
    path('form/edit_form/<int:id>/', views.edit_form, name="edit_form"),
    path('form/delete/<int:id>/', views.del_form, name="delete"),
]


