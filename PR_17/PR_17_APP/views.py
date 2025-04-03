from django.shortcuts import render, redirect
from .models import File
from .forms import FileForm

def form_up_pdf(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    form = FileForm()
    file_obj = File.objects.all()
    context = {'my_text': 'Загруженные файлы', "file_obj": file_obj, "form": form}
    return render(request, 'firstapp/form_up_pdf.html', context)

def delete_pdf(request, id):
    try:
        pdf = File.objects.get(id=id)
        pdf.delete()
        return redirect('form_up_pdf')
    except File.DoesNotExist:
        return render("NotFound")
