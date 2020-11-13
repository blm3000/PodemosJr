from django.db import models
from Clientes.models import Grupo

# Create your models here.

class Cuenta(models.Model):
    id = models.CharField(max_length =  5, primary_key = True)
    estatus = models.CharField(max_length = 15, choices = [("DESEMBOLSADA","DESEMBOLSADA"),("CERRADA","CERRADA")])
    monto = models.DecimalField(max_digits=15, decimal_places=2)
    saldo = models.DecimalField(max_digits=15, decimal_places=2)

    # establecemos relaciones entre las tablas y lo que sucede si se borra un dato
    grupo = models.ForeignKey(Grupo, on_delete = models.CASCADE)

    # created y updated nos sirven para tiener información de los registros
    # modificación y creación
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name = "cuenta"
        verbose_name_plural = "cuentas"
    
    def __str__(self):
        return self.id



class CalendarioPago(models.Model):
    #id = models.CharField(max_lenght =  5, primary_key = True)

    num_pago = models.IntegerField()
    monto = models.DecimalField(max_digits=15, decimal_places=2)
    fecha_pago = models.DateField()
    estatus = models.CharField(max_length = 15, choices =[("PENDIENTE","PENDIENTE"),("PAGADO","PAGADO"),("PARCIAL","PARCIAL"),("ATRASADO","ATRASADO")])

    cuenta = models.ForeignKey(Cuenta, on_delete = models.CASCADE)

    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now_add = True) 
    

    class Meta:
        verbose_name = "pago"
        verbose_name_plural = "pagos"
    
    # def __str__(self):
    #     return self.cuenta


class Transaccion(models.Model):
    
    fecha = models.DateTimeField()
    monto = models.DecimalField(max_digits=15, decimal_places=2)
    cuenta = models.ForeignKey(Cuenta, on_delete = models.CASCADE)
    
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name = "transaccion"
        verbose_name_plural = "transacciones"
    
    # def __str__(self):
    #     return self.cuenta



    



