from django.contrib import admin

# Importar las clases del modelo
from administrativo.models import Barrio, Casa, Persona, Departamento


class PersonaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'cedula', 'correo')
    search_fields = ('nombre', 'apellido', 'cedula', 'correo')

admin.site.register(Persona, PersonaAdmin)


class BarrioAdmin(admin.ModelAdmin): 
    list_display = ('nombre', 'siglas')
    search_fields = ('nombre', 'siglas')

admin.site.register(Barrio, BarrioAdmin)


class CasaAdmin(admin.ModelAdmin):

    list_display = ('propietario', 'direccion', 'barrio', 'color', 'val_bien', 'num_cuartos', 'num_pisos')
    search_fields = ('propietario', 'num_cuartos', 'num_pisos')

admin.site.register(Casa, CasaAdmin)


class DepartamentoAdmin(admin.ModelAdmin):

    list_display = ('propietario', 'direccion', 'barrio', 'val_bien', 'num_cuartos', 'val_mensual')
    search_fields = ('propietario', 'direccion', 'barrio', 'val_bien')

admin.site.register(Departamento, DepartamentoAdmin)