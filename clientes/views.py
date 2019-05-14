from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Cliente
from .forms import ClienteForm

# Create your views here.

@login_required #decorator para exigir login
def clientes(request):
    clientes = Cliente.objects.all()
    return render(request,'IndexListClientes.html',{'clientes':clientes})

@login_required
def novo_cliente(request):
    form = ClienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('clientes')
    return render(request,'IndexNovoCliente.html',{'form':form})

@login_required
def atualiza_cliente(request,id):
    cliente = get_object_or_404(Cliente,pk=id)
    form = ClienteForm(request.POST or None,instance=cliente)

    if form.is_valid():
        form.save()
        return redirect( 'clientes')
    return render(request,'IndexNovoCliente.html',{'form':form})

@login_required
def deleta_cliente(request,id):
    cliente = get_object_or_404(Cliente,pk=id)
    form = ClienteForm(request.POST or None,instance=cliente)

    if request.method == 'POST':
        cliente.delete()
        return redirect('clientes')

    return render(request,'confirmaDelete.html',{'form':form})

