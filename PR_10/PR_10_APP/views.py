from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Dish, Order, Category, User
from .forms import OrderForm, CategoryForm, DishForm

def index(request):
    num_categories = Category.objects.count()
    num_dishes = Dish.objects.count()
    return render(request, 'index.html', context={'num_categories': num_categories, 'num_dishes': num_dishes})

class CategoryListView(generic.ListView):
    model = Category
    template_name = 'category_list.html'

class DishDetailView(generic.DetailView):
    model = Dish
    template_name = 'dish_detail.html'

# Представления для категорий
class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category_form.html'
    success_url = reverse_lazy('categories')

class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category_form.html'
    success_url = reverse_lazy('categories')

# Представления для блюд
class DishCreateView(CreateView):
    model = Dish
    form_class = DishForm
    template_name = 'dish_form.html'
    success_url = reverse_lazy('dish-list')

class DishUpdateView(UpdateView):
    model = Dish
    form_class = DishForm
    template_name = 'dish_form.html'
    success_url = reverse_lazy('dish-list')


class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'order_form.html'
    success_url = reverse_lazy('my-orders')  # Указываем URL для успешного создания

    def form_valid(self, form):
        form.instance.customer = self.request.user
        return super().form_valid(form)

class MyOrdersView(LoginRequiredMixin, generic.ListView):
    model = Order
    template_name = 'my_orders.html'
    paginate_by = 10

    def get_queryset(self):
        return Order.objects.filter(customer=self.request.user).order_by('-date_ordered')
