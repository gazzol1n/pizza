
from PR_3_APP import views
from django.urls import path

urlpatterns = [
    path('index/', views.index),
    path('index1/', views.index1),
    path('index2/', views.index2),
]
