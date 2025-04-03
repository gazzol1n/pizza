from django.shortcuts import render
from django.views import generic
from .models import Category, Dish

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
