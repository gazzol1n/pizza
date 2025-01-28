from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, "index.html")


def index1(request):
    data = {"age": 50}
    return render(request, "index1.html", context=data)

def index2(request):
    cat = ["Ноутбуки", "Принтеры", "Сканеры", "Диски", "Шнуры"]
    return render(request, "index2.html", context={"cat": cat})

# Create your views here.
