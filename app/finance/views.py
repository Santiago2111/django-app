from django.shortcuts import render
from django.http import HttpResponse
from .models import Cliente
from .models import Transaccion

# Create your views here.

def list_clientes(request):
    #return HttpResponse("Here you find a list of users")
    clientes = Cliente.objects.all()
    return render(request, 'finance/list_client.html', {'clientes': clientes})

def list_transacciones(request):
    #return HttpResponse("Here you find a list of users")
    transacciones = Transaccion.objects.all()
    return render(request, 'finance/list_transaccion.html', {'transacciones': transacciones})
