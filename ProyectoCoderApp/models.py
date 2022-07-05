from django.db import models

# Create your models here.

class Maquinaria(models.Model):

    # id por defecto
    marca = models.CharField(max_length=30) # Texto
    funcion = models.CharField(max_length=30)

class Herramientas(models.Model):

    # id por defecto
    codigo = models.IntegerField() 
    tipo = models.CharField(max_length=30) # Texto
    marca = models.CharField(max_length=30) # Texto
    

class Operario(models.Model):

    # id por defecto
    nombre = models.CharField(max_length=30) # Texto
    apellido = models.CharField(max_length=30) # Texto
    area = models.CharField(max_length=30)

    # dni = models.IntegerField()

    class Meta:
        verbose_name_plural = "Operarios"

class Entregable(models.Model):

    nombre = models.CharField(max_length=30)
    fechaEntrega = models.DateField()
    entregado = models.BooleanField()

    def __str__(self) -> str: # modificar como se visualiza
        return f"Entregable: {self.nombre} en la fecha {self.fechaEntrega}"