# Archivo views para controlar los direccionamientos de la aplicación "Cuentas"

from django.shortcuts import render, HttpResponse
from cuentas.models import Cuenta, CalendarioPago, Transaccion # importamos los modelos
# Create your views here.


# la pagina principal que mostrará los el template principal
def home(request):
    return render(request,"cuentas/home.html")


# vista que sirve para mostrar los datos de las cuentas 
def cuentas(request):
    pagos_all = CalendarioPago.objects.all()
    trans_all = Transaccion.objects.all()
    
    return render(request,"cuentas/cuentas.html",{"pagos": pagos_all, "transacciones": trans_all})

# vista que controla lo que pasa cuando se agrega un nuevo pago
def agregarPago(request):
    if request.method == 'POST':
            
        if request.POST.get('PnCuenta'):
            condiciona = request.POST.get('PnPago') and request.POST.get('PnMonto') and request.POST.get('PnFecha') and request.POST.get('recipient-name')
            if condiciona:
                cuenta = request.POST.get('PnCuenta')
                #print(f"cuenta: {cuenta}")
                saldo = Cuenta.objects.get(pk = int(cuenta))
                #print(f"saldo {saldo.saldo}")
                total = saldo.saldo
                if total < 0:
                    return HttpResponse("Pago no registrado!, cuenta no tiene saldo pendiente")
                elif total < float(request.POST.get('PnMonto')):
                    return HttpResponse("El pago excede el total por pagar!")
                else: # hacemos insert de pago
                    nuevo_Pago = CalendarioPago()
                    
                    nuevo_Pago.cuenta = saldo #request.POST.get('PnCuenta')
                    nuevo_Pago.num_pago = int(request.POST.get('PnPago'))
                    nuevo_Pago.monto = float(request.POST.get('PnMonto'))
                    nuevo_Pago.fecha_pago = request.POST.get('PnFecha')
                    nuevo_Pago.estatus = request.POST.get('recipient-name')
                    nuevo_Pago.save()
                    #return HttpResponse("El pago se registró exitosamente!")
                    return cuentas(request)

