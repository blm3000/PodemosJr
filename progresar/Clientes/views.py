# Archivo views para controlar los direccionamientos de la aplicación "clientes"

from django.shortcuts import render,HttpResponse
from Clientes.models import Cliente, Grupo # importamos los modelos

# Create your views here.

# este vista se encarga de manejar la url clientes
def clientes(request):
    # obtenemos todos los clientes registrados
    clientes_all = Cliente.objects.all()

    # regresamos la plantilla de los clientes y enviamos todos los clientes que se encuentran existentes
    return render(request, "clientes/clientes.html", {"clientes": clientes_all})

# para mostrar los grupos
def grupos(request):

    grupos_all = Grupo.objects.all()
    return render(request, "Clientes/grupos.html", {"grupos": grupos_all})

# view para controlar las creaciones de nuevos clientes
def agregarCliente(request):
    if request.method == 'POST':
        # verificamos que los campos necesarios tengan valore
        if request.POST.get('newId') and request.POST.get('newNombre'):
            # creamos un nuevo objeto del modelo clientes
             nuevo_cliente = Cliente()
             # Agregamos atributos
             nuevo_cliente.id = request.POST.get('newId')
             nuevo_cliente.nombre = request.POST.get('newNombre')
             nuevo_cliente.save() # lo guardamos 

             return clientes(request)
        else: 
            return HttpResponse("Llene todos los campos!")


def modificarCliente(request):

    if request.method == 'POST':
    
        # verificamos que los campos necesarios tengan valore
        if request.POST.get('todoId') and request.POST.get('todoName'):
    
            # creamos un nuevo objeto del modelo clientes
            modificar_cliente = Cliente.objects.get(pk = request.POST.get('todoId'))

            modificar_cliente.nombre = request.POST.get('todoName')
            print(f"nuevo nombre = {modificar_cliente}")
            modificar_cliente.save() # lo guardamos 

            return clientes(request)
            
        else: 
            return HttpResponse("Llene todos los campos!")


def agregarCaGrupo(request, id = None):
    # grupoMiembros = Grupo.objects.get(pk = id)
    grupoMiembros = Grupo.objects.get(id = id)
    # print( grupoMiembros.nombre)
    # print( type(grupoMiembros.clientes))
    # print( grupoMiembros.clientes.all())
    miembros = []
    for cliente in grupoMiembros.clientes.all():
        miembros.append(cliente.nombre)
        #print(miembros)
    clientesNo = Cliente.objects.exclude(nombre__in=miembros)

    return render(request, 'Clientes/modalAgregarCliente.html', {'otrosMiembros': clientesNo,"grupoId":id})


# se encarga de guardar la información
def guardaGrupoClientes(request):
    if request.method == 'POST':
        grupo = request.POST.get('grupo-id') # traemos el valor del grupo seleccionado
        grupo_insertar = Grupo.objects.get(id = grupo) #buscamos la instacia en la base para ese grupo

        clientes_nuevos = request.POST.getlist('clientes-select') #nos traemos el valor de los clientes seleccionados
        
        for cliente in clientes_nuevos:
            cliente_insertar =  Cliente.objects.get(id = cliente) # obtenemos la instancia de la  base para cada cliente seleccionado
            grupo_insertar.clientes.add(cliente_insertar) # agrewgamos a grupo la instancia del cliente
    
    return grupos(request)

