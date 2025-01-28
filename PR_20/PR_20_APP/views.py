from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse
from .models import Author, BookInstance
from .forms import Form_add_author
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


# Представление для списка заказанных книг
class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    model = BookInstance
    template_name = 'bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='2').order_by('due_back')

# Редактирование авторов
def edit_authors(request):
    author = Author.objects.all()
    context = {'author': author}
    return render(request, "edit_authors.html", context)

# Добавление нового автора
def add_author(request):
    if request.method == 'POST':
        form = Form_add_author(request.POST, request.FILES)
        if form.is_valid():
            obj = Author.objects.create(
                first_name=form.cleaned_data.get("first_name"),
                last_name=form.cleaned_data.get("last_name"),
                date_of_birth=form.cleaned_data.get("date_of_birth"),
                about=form.cleaned_data.get("about"),
                photo=form.cleaned_data.get("photo")
            )
            obj.save()
            return HttpResponseRedirect(reverse('authors-list'))
    else:
        form = Form_add_author()
    context = {"form": form}
    return render(request, "authors_add.html", context)

# Удаление автора
def delete(request, id):
    try:
        author = Author.objects.get(id=id)
        author.delete()
        return HttpResponseRedirect("/edit_authors/")
    except:
        return HttpResponseNotFound("<h2>Автор не найден</h2>")


from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.conf import settings
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.models import User

# Вход
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')  # Перенаправление на главную страницу
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# Регистрация
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')  # Перенаправление на главную страницу
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

# Восстановление пароля
def password_reset_request(request):
    if request.method == "POST":
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            # Генерация токена для восстановления пароля
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(str(user.pk).encode())
            # Отправка ссылки для восстановления пароля на email
            reset_link = f"http://localhost:8000/password_reset/{uid}/{token}/"
            send_mail(
                "Сброс пароля",
                f"Перейдите по следующей ссылке, чтобы сбросить пароль: {reset_link}",
                settings.EMAIL_HOST_USER,
                [email],
            )
            return redirect('password_reset_done')  # Страница с подтверждением отправки
        except User.DoesNotExist:
            # Если пользователя с таким email нет, выводим ошибку
            return redirect('password_reset_failed')  # Страница с ошибкой
    return render(request, 'password_reset.html')
