from django import forms
from ConciertoApp.models import Entrada, Persona, Concierto
from itertools import cycle
from datetime import date, datetime

class FormEntrada(forms.ModelForm):
    class Meta:
        model = Entrada
        fields = ['concierto', 'persona', 'Categoria', 'Descripcion', 'NumeroAsiento', 'Precio', 'Sector']
    
    def clean_Descripcion(self):
        descripcion = self.cleaned_data['Descripcion']
        if len(descripcion) > 200:
            raise forms.ValidationError("La descripción no puede tener más de 200 caracteres.")
        return descripcion
    

class FormPersona(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['RUT', 'Nombre', 'Apellido', 'Telefono', 'Correo']

    def clean_Nombre(self):
        inputNombre = self.cleaned_data['Nombre']
        if len(inputNombre) > 20:
            raise forms.ValidationError("El largo maximo del nombre son 20 caracteres")
        return inputNombre
    
    def clean_Apellido(self):
        inputApellido = self.cleaned_data['Apellido']
        if len(inputApellido) > 20:
            raise forms.ValidationError("El largo maximo del apellido son 20 caracteres")
        return inputApellido
    
    def clean_correo(self):
        email = self.cleaned_data['Correo']
        if email.find('@') == -1:
            raise forms.ValidationError("El correo debe contener @")
        return email


class FormConcierto(forms.ModelForm):
    class Meta:
        model = Concierto
        fields = ['Fecha', 'Hora', 'Lugar', 'Categoria', 'Capacidad']

    def clean_Capacidad(self):
        capacidad = self.cleaned_data['Capacidad']
        if capacidad <= 0:
            raise forms.ValidationError("La capacidad debe ser un número positivo.")
        if capacidad > 100000:  
            raise forms.ValidationError("La capacidad parece ser irrealmente alta.")
        return capacidad