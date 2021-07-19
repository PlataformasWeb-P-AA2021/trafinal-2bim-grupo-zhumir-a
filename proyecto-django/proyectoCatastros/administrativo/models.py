from django.db import models

# Create your models here.
class Barrio(models.Model):
    nombre = models.CharField("Nombre del barrio", max_length=50)
    siglas = models.CharField("Siglas", max_length=20)

    def __str__(self):
        return "%s - %s" % {
            self.nombre,
            self.siglas
        }

class Persona(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    cedula = models.CharField(max_length=10)
    correo = models.CharField(max_length=30)

    def __str__(self):
        return "%s - %s - %s - %s" % {
            self.nombre,
            self.apellido,
            self.cedula,
            self.correo
        }

class Casa(models.Model):
    propietario = models.ForeignKey(Persona, on_delete=models.CASCADE,
            related_name="personaCasa") # Tipo Persona
    direccion = models.CharField("Dirección de la casa", max_length=60)
    barrio = models.ForeignKey(Barrio, on_delete=models.CASCADE,
            related_name="barrioCasa")# Tipo Barrio
    val_bien = models.FloatField("Valor del bien")
    color = models.CharField("Color del Inmueble", max_length=20)
    num_cuartos = models.IntegerField("Número de cuartos")
    num_pisos = models.IntegerField("Número de pisos")

    def __str__(self):
        return "Propietario: %s | Direccion: %s - valor: $%.2f | %s - cuartos: %d  - pisos:  %d " % {
            self.propietario,
            self.direccion,
            self.val_bien,
            self.color,
            self.num_cuartos,
            self.num_pisos
        }

class Departamento(models.Model):
    propietario = models.ForeignKey(Persona, on_delete=models.CASCADE,
            related_name="personaDept") # Tipo Persona
    direccion = models.CharField("Dirección de la casa", max_length=60)
    barrio = models.ForeignKey(Barrio, on_delete=models.CASCADE,
            related_name="barrioDept")# Tipo Barrio
    val_bien = models.FloatField("Valor del bien")
    num_cuartos = models.IntegerField("Número de cuartos")
    val_mensual = models.FloatField("Valor mensual de mantenimiento")

    def __str__(self):
        return "Propietario: %s | Direccion: %s - Valor bien: $%.2f | %s - cuartos: %d  - Valor mensual:  %d " % {
            self.propietario,
            self.direccion,
            self.val_bien,
            self.num_cuartos,
            self.val_mensual
        }
