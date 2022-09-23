from django.http import HttpResponse
from django.shortcuts import render

import proyectoFinal_app
from proyectoFinal_app.models import *

# Create your views here.

def inicio(request):
    return render(request,'proyectoFinal_app/inicio.html')

def user(request):
    return render(request,('proyectoFinal_app/usuario.html'))

def computer(request):
    return render(request,('proyectoFinal_app/computadoras.html'))

def cellphone(request):
    return render(request,('proyectoFinal_app/celulares.html'))

def printer(request):
    return render(request,('proyectoFinal_app/impresoras.html'))

def router(request):
    return render(request,('proyectoFinal_app/routers.html'))

def stockForm(request):
    if request.method== "POST":
        stock=salecomputer(computerBrand=request.POST["Item"], computerQty=request.POST["Cantidad"])
        stock.save()
        return render(request, "proyectoFinal_app/inicio.html")
    return render(request,('proyectoFinal_app/stock.html'))