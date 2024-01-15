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
