# Clientes/resources.py
# librerias necesarias para hacer uso de la api
from tastypie.resources import ModelResource
from Clientes.models import Cliente

# clase que sevirá para mostrar los resultados de todos los registros de clientes utilizando la "api"
class ClienteRecurso(ModelResource):
    class Meta:
        queryset = Cliente.objects.all()
        resource_name = 'clientes'