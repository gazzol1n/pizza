from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Book, Author, BookInstance

def index(request): 
    text_head = 'На нашем сайте вы можете получить книги в электронном виде' 
    books = Book.objects.all() 
    num_books = Book.objects.all().count() 
 
    num_instances = BookInstance.objects.all().count() 
    num_instances_available = BookInstance.objects.filter(status__exact=2).count()  
    authors = Author.objects 
    num_authors = Author.objects.count() 
 
    # Словарь для передачи данных в шаблон index.html 
    context = {'text_head': text_head, 
               'books': books, 'num_books': num_books, 
               'num_instances': num_instances, 
               'num_instances_available': num_instances_available, 
               'authors': authors, 'num_authors': num_authors} 
    return render(request, 'firstapp/index.html', context) 


class BookListView(ListView):
    model = Book
    context_object_name = 'books'
    paginate_by = 3 

class AuthorListView(ListView):
    model = Author 
    paginate_by = 4 

class AuthorDetailView(DetailView):     
    model = Author 

class BookDetailView(DetailView):
    model = Book
    context_object_name = 'book'
