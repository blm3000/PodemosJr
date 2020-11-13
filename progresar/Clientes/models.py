# este archivo se encarga de gestionar los modelos para la app "clientes"
from django.db import models

# Create your models here.

# creamos un modelo utilizando ORM para gestión de la DB y el modelo
class Cliente(models.Model):
    # de claración de lostipos de dato y sus nombres
    id = models.CharField(max_length = 7, primary_key =True)
    nombre = models.CharField(max_length = 60)

    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now_add = True)

    # asignamos nombres en singular y plural para el panel de administración
    class Meta:
        verbose_name = "cliente"
        verbose_name_plural = "clientes"
    
    # sobre escribirmos el método  str para que entregue el nombre
    def __str__(self):
        return self.nombre


class Grupo(models.Model):
    id = models.CharField(max_length = 5, primary_key = True)
    nombre = models.CharField(max_length = 50)

    # establecemos una relación muchos a muchos para que DJAgo
    # cree una tabla intermedia
    clientes = models.ManyToManyField(Cliente)

    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now_add = True)


    class Meta:
        verbose_name = "grupo"
        verbose_name_plural = "grupos"
    
    def __str__(self):
        return self.nombre

# class Clientes_grupo_clientes(models.Model):
#     grupo_id = models.ForeignKey(Grupo, on_delete=models.CASCADE)
#     cliente_id = models.ForeignKey(Cliente, on_delete=models.CASCADE)