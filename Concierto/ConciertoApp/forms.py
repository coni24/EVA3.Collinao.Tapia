from django import forms
from ConciertoApp.models import Entrada, Persona, Concierto

class FormEntrada(forms.ModelForm):
    class Meta:
        model = Entrada
        fields = '__all__'

class FormPersona(forms.ModelForm):
    class Meta:
        model = Persona
        fields = '__all__'

class FormConcierto(forms.ModelForm):
    class Meta:
        model = Concierto
        fields = '__all__'