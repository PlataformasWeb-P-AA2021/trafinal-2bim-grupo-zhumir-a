from django.db import models

# Create your models here.
class Barrio(models.Model):
    nombre = models.CharField("Nombre del barrio", max_length=50),
    siglas = models.CharField(max_length=50)

    def __str__(self):
        return "%s - %s" % {
            self.nombre,
            self.ciudad
        }

class Persona(models.Model):
    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    cedula = models.CharField(max_length=10)
    correo = models.CharField(max_length=30)

    def __str__(self):
        return "%s - %s" % {
            self.nombre,
            self.cedula
        }

class Casas(models.Model):
    propietario = models.Persona("Nombre del propetario", max_length=60) # Tipo Persona
    direccion = models.CharField("Dirección de la casa", max_length=60)
    barrio = models.Barrio(max_length=50) # Tipo Barrio
    val_bien = models.FloatField("Valor del bien")
    color = models.CharField("Color del Inmueble", max_length=20)
    num_cuartos = models.IntegerField("Número de cuartos")
    num_pisos = models.IntegerField("Número de pisos")

    def __str__(self):
        return "%s | %s - %s - $%.2f | %s - %d cuartos - %d pisos" % {
            self.propietario,
            self.direccion,
            self.barrio,
            self.val_bien,
            self.color,
            self.num_cuartos,
            self.num_pisos
        }

class Departamento(models.Model):
    propietario = models.Persona("Nombre del propetario", max_length=60) # Tipo Persona
    direccion = models.CharField("Dirección de la casa", max_length=60)
    barrio = models.Barrio(max_length=50) # Tipo Barrio
    val_bien = models.FloatField("Valor del bien")
    num_cuartos = models.IntegerField("Número de cuartos")
    val_mensual = models.FloatField("Valor mensual de mantenimiento")

    def __str__(self):
        return "%s | %s - %s - $%.2f | %s - %d cuartos - %d pisos" % {
            self.propietario,
            self.direccion,
            self.barrio,
            self.val_bien,
            self.color,
            self.num_cuartos,
            self.num_pisos
        }
