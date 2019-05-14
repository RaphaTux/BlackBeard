
#views do projeto
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required()
def hello(request):
    return  HttpResponse( 'Olá mundo ')

@login_required()
def clientes(request):
    return  render(request,'IndexCliente.html')

