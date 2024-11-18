from django import forms
from ConciertoApp.models import Entrada, Persona, Concierto
from itertools import cycle
from datetime import date, datetime
from django.core.exceptions import ValidationError

class FormEntrada(forms.ModelForm):
    class Meta:
        model = Entrada
        fields = ['concierto', 'persona', 'Descripcion', 'NumeroAsiento', 'Precio', 'Sector']
    
    def clean_Precio(self):
        precio = self.cleaned_data['Precio']
        if precio <= 0:
            raise forms.ValidationError("El precio no puedo ser negativo.")
        return precio
    
    def clean_NumeroAsiento(self):
        numAsiento = self.cleaned_data['NumeroAsiento']
        if numAsiento <= 0:
            raise forms.ValidationError("El Número de Asiento no puedo ser negativo.")
        return numAsiento

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
        return capacidad
    
    def clean_fecha(self):
        fecha = self.cleaned_data['Fecha']
        if fecha < date.today():
            raise ValidationError("La fecha no puede ser una fecha anterior")
        return fecha
    
    def clean_hora(self):
        hora = self.cleaned_data['Hora']
        if not isinstance(hora, datetime.time):
            raise ValidationError('La hora debe estar en un formato válido.')
        return hora
    