from django.urls import path
from proyectoFinal_app.models import *
from proyectoFinal_app.views import *

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('usuario/', user, name="Usuario"),
    path('computadoras/', computer, name="Computadoras"),
    path('celulares/', cellphone, name="Celulares"),
    path('impresoras/', printer, name="Impresoras"),
    path('routers/', router, name="Routers"),
    path('stock/', stockForm, name="Stock")
]

