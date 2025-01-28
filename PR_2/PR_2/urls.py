from PR_2_APP import views
from django.urls import path

urlpatterns = [
    path('products/<int:productid>/', views.products),
    path('users/<int:id>/<str:name>/', views.users),
]
