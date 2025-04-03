from django.urls import path
from django.contrib import admin
from PR_9_APP import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('categories/', views.CategoryListView.as_view(), name='categories'),
    path('dishes/<int:pk>', views.DishDetailView.as_view(), name='dish-detail'),
]
