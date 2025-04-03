from django.shortcuts import render
from .forms import UserForm

def user_form_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            # Обработка данных формы, если необходимо
            form_data = form.cleaned_data  # Получить данные
            return render(request, 'form_success.html', {'form_data': form_data})
    else:
        form = UserForm()
    return render(request, 'user_form.html', {'form': form})
