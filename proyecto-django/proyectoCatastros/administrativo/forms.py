from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from django import forms


from administrativo.models import Casa, \
        Departamento, Persona, Barrio

class PersonaForm(ModelForm):
    class Meta:
        model = Persona
        fields = ['nombre', 'apellido', 'cedula', 'correo']
        labels = {
            'nombre': _('Ingrese los nombres por favor'),
            'apellido': _('Ingrese los  apellidos por favor'),
            'cedula': _('Ingrese la cédula por favor'),
            'correo': _('Ingrese el correo por favor'),
        }

    # Validacion de nmbre, apellido, cedula, correo
    def clean_nombre(self):
        valor = self.cleaned_data['nombre']
        num_palabras = len(valor.split())
        """
        """
        if num_palabras < 2:
            raise forms.ValidationError("Ingrese dos nombre por favor")
        return valor

    def clean_apellido(self):
        valor = self.cleaned_data['apellido']
        num_palabras = len(valor.split())

        if num_palabras < 2:
            raise forms.ValidationError("Ingrese dos apellidos por favor")
        return valor

    def clean_cedula(self):
        valor = self.cleaned_data['cedula']
        if len(valor) != 10:
            raise forms.ValidationError("Ingrese cédula con 10 dígitos")
        return valor

    def clean_correo(self):
        valor = self.cleaned_data['correo']
        if "@" not in valor or "utpl.edu.ec" not in valor:
            raise forms.ValidationError("Ingrese correo válido para la Universidad")
        return valor


class BarrioForm(ModelForm):
    class Meta:
        model = Barrio
        fields = ['nombre', 'siglas']
        labels = {
            'nombre': _('Ingrese el nombre por favor'),
            'siglas': _('Ingrese las siglas por favor'),
         
        }



class DepartamentoForm(ModelForm):
    class Meta:
        model = Departamento
        fields = ['propietario', 'direccion', 'barrio', 'val_bien', 'num_cuartos', 'val_mensual']
        labels = {
            'propietario': _('Ingrese los nombres del propietario'),
            'direccion': _('Ingrese la dirección'),
            'barrio': _('Ingrese el barrio al que pertenece'),
            'val_bien': _('Ingrese el valor del bien'),
            'num_cuartos': _('Ingrese el número de cuartos'),
            'val_mensual': _('Ingrese el valor mensual de mantenimiento'),
        }


   
class CasaForm(ModelForm):
    class Meta:
        model = Casa
        fields = ['propietario', 'direccion', 'barrio', 'color', 'val_bien', 'num_cuartos', 'num_pisos']
        labels = {
            'propietario': _('Ingrese los nombres del propietario'),
            'direccion': _('Ingrese la dirección'),
            'barrio': _('Ingrese el barrio al que pertenece'),
            'val_bien': _('Ingrese el valor del bien'),
            'color': _('Ingrese el color del inmueble'),
            'num_cuartos': _('Ingrese el número de cuartos'),
            'num_pisos': _('Ingrese el número de pisos de la casa'),
        }
