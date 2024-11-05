from django import forms
from ConciertoApp.models import Entrada, Persona, Concierto
from itertools import cycle
from datetime import date, datetime

class FormEntrada(forms.ModelForm):
    class Meta:
        model = Entrada
        fields = ['concierto', 'persona', 'Categoria', 'Descripcion', 'NumeroAsiento', 'Precio', 'Sector']

    def clean_Categoria(self):
        categoria = self.cleaned_data['Categoria']
        if not categoria.isalpha():
            raise forms.ValidationError("La categoría debe contener solo letras.")
        if len(categoria) > 20:
            raise forms.ValidationError("La categoría no puede tener más de 20 caracteres.")
        return categoria
    
    def clean_Descripcion(self):
        descripcion = self.cleaned_data['Descripcion']
        if len(descripcion) > 200:
            raise forms.ValidationError("La descripción no puede tener más de 200 caracteres.")
        return descripcion
    
    def clean_NumeroAsiento(self):
        numero_asiento = self.cleaned_data['NumeroAsiento']
        if numero_asiento <= 0:
            raise forms.ValidationError("El número de asiento debe ser un número positivo.")
        concierto = self.cleaned_data.get('Concierto')
        if concierto and Entrada.objects.filter(Concierto=concierto, NumeroAsiento=numero_asiento).exists():
            raise forms.ValidationError("Este número de asiento ya está asignado para este concierto.")
        return numero_asiento
    
    def clean_Precio(self):
        precio = self.cleaned_data['Precio']
        if precio <= 0:
            raise forms.ValidationError("El precio debe ser un valor positivo.")
        return precio

class FormPersona(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['RUT', 'Nombre', 'Apellido', 'Telefono', 'Edad', 'Correo']

#VALIDAR RUT
    def clean_RUT(self):
        rut = self.cleaned_data['RUT']
        reversed_digits = map(int, reversed(str(rut)))
        factors = cycle(range(2, 8))
        s = sum(d * f for d, f in zip(reversed_digits, factors))
        return (-s) % 11

    def clean_Nombre(self):
        nombre = self.cleaned_data['Nombre']
        if len(nombre) > 20:
            raise forms.ValidationError("El largo maximo del nombre son 20 caracteres")
        if not nombre.replace(" ", "").isalpha():
            raise forms.ValidationError("El nombre solo debe contener letras.")
        return nombre
    
    def clean_Apellido(self):
        apellido = self.cleaned_data['Apellido']
        if len(apellido) > 20:
            raise forms.ValidationError("El largo maximo del apellido son 20 caracteres")
        if not apellido.replace(" ", "").isalpha():
            raise forms.ValidationError("El apellido solo debe contener letras.")
        return apellido
    
    def clean_Telefono(self):
        telefono = self.cleaned_data['Telefono']
        if not telefono.isdigit():
            raise forms.ValidationError("El teléfono solo debe contener números.")
        if len(telefono) != 9:
            raise forms.ValidationError("El teléfono debe tener exactamente 9 dígitos.")
        if telefono[0] != '9':
            raise forms.ValidationError("El teléfono debe comenzar con el número 9.")
        return telefono
    
    def clean_Edad(self):
        edad = self.cleaned_data['Edad']
        if edad < 16 or edad > 80:
            raise forms.ValidationError("La edad debe estar entre 16 y 80 años.")
        return edad
    
    def clean_correo(self):
        email = self.cleaned_data['Correo']
        if email.find('@') == -1:
            raise forms.ValidationError("El correo debe contener @")
        return email

class FormConcierto(forms.ModelForm):
    class Meta:
        model = Concierto
        fields = ['Fecha', 'Hora', 'Lugar', 'Categoria', 'Capacidad']

    def clean_Fecha(self):
        fecha = self.cleaned_data['Fecha']
        if fecha < date.today():
            raise forms.ValidationError("La fecha no puede ser en el pasado.")
        return fecha

    def clean_Hora(self):
        hora = self.cleaned_data['Hora']
        # Se puede agregar validación de rango de horas según las necesidades
        if hora < datetime.time(9, 0) or hora > datetime.time(23, 0):
            raise forms.ValidationError("La hora debe estar entre las 9:00 y las 23:00.")
        return hora


    def clean_Categoria(self):
        categoria = self.cleaned_data['Categoria']
        if not categoria.isalpha():
            raise forms.ValidationError("La categoría debe contener solo letras.")
        if len(categoria) > 20:
            raise forms.ValidationError("La categoría no puede tener más de 20 caracteres.")
        return categoria

    def clean_Capacidad(self):
        capacidad = self.cleaned_data['Capacidad']
        if capacidad <= 0:
            raise forms.ValidationError("La capacidad debe ser un número positivo.")
        if capacidad > 100000:  
            raise forms.ValidationError("La capacidad parece ser irrealmente alta.")
        return capacidad