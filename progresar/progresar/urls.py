"""progresar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Clientes.resources import ClienteRecurso

# creamos una instancia de la api
cliente_resource = ClienteRecurso()


# aquí guardamos las direcciones url que aparecen en el navegador
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cuentas.urls')),
    path('', include('Clientes.urls')),
    # path('clientes/modificarCliente/', include('Clientes.urls')),
    # path('clientes/agregarCliente/',include('Clientes.urls')),
    # path('clientes/agregarCliente/',include('Clientes.urls')),
    # path('clientes/agregarCaGrupo/',include('Clientes.urls')),
    #path('clientes/guardaGrupoClientes/', include('Clientes.urls')),
    # todo lo que inicie "api" consumirá el servicio de la api
    path('api/', include(cliente_resource.urls)),
    #path('home/', views.home, name = 'home')
]
