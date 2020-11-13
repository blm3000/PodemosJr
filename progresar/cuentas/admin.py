from django.contrib import admin
from .models import Cuenta,CalendarioPago,Transaccion

# Register your models here.

class CuentaAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")

class CalendarioPagoAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")
    list_display = ("cuenta", "num_pago", "monto", "fecha_pago", "estatus", "updated")

class TransaccionAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")
    list_display = ("cuenta", "fecha", "monto", "updated")



admin.site.register(Cuenta, CuentaAdmin)
admin.site.register(CalendarioPago, CalendarioPagoAdmin)
admin.site.register(Transaccion, TransaccionAdmin)