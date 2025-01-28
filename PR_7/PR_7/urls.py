from django.urls import path
from PR_7_APP import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_person/', views.create_person, name='create_person'),
    path('create_category/', views.create_category, name='create_category'),
    path('create_dish/', views.create_dish, name='create_dish'),
    path('edit_person/<int:id>/', views.edit_person, name='edit_person'),
    path('edit_category/<int:id>/', views.edit_category, name='edit_category'),
    path('edit_dish/<int:id>/', views.edit_dish, name='edit_dish'),
    path('delete_person/<int:id>/', views.delete_person, name='delete_person'),
    path('delete_category/<int:id>/', views.delete_category, name='delete_category'),
    path('delete_dish/<int:id>/', views.delete_dish, name='delete_dish'),
]
