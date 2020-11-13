from django.urls import path
from cuentas import views

# urls personales de applicación
urlpatterns = [
    path('', views.home, name = 'Home'),
    path('cuentas/',views.cuentas, name ='Cuentas'),
    path('agregarPago/',views.agregarPago,name = 'agregarPago'),
    
]
