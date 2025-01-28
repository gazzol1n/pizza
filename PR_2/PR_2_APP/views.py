from django.shortcuts import HttpResponse

def products(request, productid):
    output = "<h2>Продукт</h2> №{0}".format(productid)
    return HttpResponse(output)

def users(request, id, name):
    output = "<h2>Пользователь</h2> Имя: {0} ID: {1}".format(name, id)
    return HttpResponse(output)