from django import forms

from . import models

class PersonaForm(forms.ModelForm):
    class Meta:
        model = models.Persona
        fields = '__all__'


