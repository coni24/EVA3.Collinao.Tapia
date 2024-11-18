from django.contrib import admin
from ConciertoApp.models import Entrada, Persona, Concierto
from ConciertoApp.forms import FormEntrada, FormPersona, FormConcierto

class EntradaAdmin(admin.ModelAdmin):
    form = FormEntrada

class PersonaAdmin(admin.ModelAdmin):
    form = FormPersona

class ConciertoAdmin(admin.ModelAdmin):
    form = FormConcierto

admin.site.register(Entrada, EntradaAdmin)
admin.site.register(Persona, PersonaAdmin)
admin.site.register(Concierto, ConciertoAdmin)
