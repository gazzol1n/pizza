from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from PR_10_APP import views
from PR_10_APP.views import CategoryCreateView, CategoryUpdateView, DishCreateView, DishUpdateView

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('categories/', views.CategoryListView.as_view(), name='categories'),
    path('dishes/<int:pk>', views.DishDetailView.as_view(), name='dish-detail'),
    path('order/new/', views.OrderCreateView.as_view(), name='order-create'),
    path('orders/', views.MyOrdersView.as_view(), name='my-orders'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
     # Категории
    path('category/new/', CategoryCreateView.as_view(), name='category-create'),
    path('category/edit/<int:pk>/', CategoryUpdateView.as_view(), name='category-update'),
    
    # Блюда
    path('dish/new/', DishCreateView.as_view(), name='dish-create'),
    path('dish/edit/<int:pk>/', DishUpdateView.as_view(), name='dish-update'),
]
