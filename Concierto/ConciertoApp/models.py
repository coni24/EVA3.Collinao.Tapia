from django.db import models


class Persona(models.Model):
    RUT = models.CharField(max_length=9,unique=True)
    Nombre = models.CharField(max_length=20)
    Apellido = models.CharField(max_length=20)
    Telefono = models.CharField(max_length=9)
    Correo = models.EmailField()

    def __str__(self):
        return f"{self.Nombre} {self.Apellido}"

class Concierto(models.Model):
    Fecha = models.DateField(default="2024-10-31")
    Hora = models.TimeField(default="11:00")
    Lugar = models.CharField(max_length=100)
    Categoria = models.CharField(max_length=15)
    Capacidad = models.IntegerField()

    def __str__(self):
        return f"{self.Lugar} - {self.Fecha}"
    
class Entrada(models.Model):
    Descripcion = models.CharField(max_length = 50)
    NumeroAsiento = models.IntegerField(default=1)
    Precio = models.IntegerField()
    Sector = models.CharField(max_length = 50)
    concierto = models.ForeignKey(Concierto, on_delete=models.CASCADE)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.persona} - Asiento {self.NumeroAsiento}"