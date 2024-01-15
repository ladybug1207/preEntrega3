from django import forms

from . import models

class PersonaForm(forms.ModelForm):
    class Meta:
        model = models.Persona
        fields = '__all__'

class ClienteForm(forms.ModelForm):
    class Meta:
        model = models.Cliente
        fields = '__all__'

class ProductoForm(forms.ModelForm):
    class Meta:
        model = models.Producto
        fields = '__all__'

class VendedorForm(forms.ModelForm):
    class Meta:
        model = models.Vendedor
        fields = '__all__'