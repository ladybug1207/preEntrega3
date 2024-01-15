from django.shortcuts import render
from django.shortcuts import redirect

from . import models
from . import forms

# Create your views here.

def index(request):
    return render(request, 'Aplicacion/index.html')

def persona_list(request):
    consulta = models.Persona.objects.all()
    contexto = {'personas': consulta}
    return render(request, 'Aplicacion/persona_list.html', contexto)

def persona_create(request):
    if request.method == 'POST':
        form = forms.PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('persona_list')
    else:
        form = forms.PersonaForm()
    return render(request, 'Aplicacion/persona_create.html', {'form':form})

def cliente_list(request):
    consulta = models.Cliente.objects.all()
    contexto = {'clientes': consulta}
    return render(request, 'Aplicacion/cliente_list.html', contexto)

def cliente_create(request):
    if request.method == 'POST':
        form = forms.ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cliente_list')
    else:
        form = forms.ClienteForm()
    return render(request, 'Aplicacion/cliente_create.html', {'form':form})

def producto_list(request):
    consulta = models.Producto.objects.all()
    contexto = {'productos': consulta}
    return render(request, 'Aplicacion/producto_list.html', contexto)

def producto_create(request):
    if request.method == 'POST':
        form = forms.ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('producto_list')
    else:
        form = forms.ProductoForm()
    return render(request, 'Aplicacion/producto_create.html', {'form':form})

def vendedor_list(request):
    consulta = models.Vendedor.objects.all()
    contexto = {'vendedores': consulta}
    return render(request, 'Aplicacion/vendedor_list.html', contexto)

def vendedor_create(request):
    if request.method == 'POST':
        form = forms.VendedorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vendedor_list')
    else:
        form = forms.VendedorForm()
    return render(request, 'Aplicacion/vendedor_create.html', {'form':form})