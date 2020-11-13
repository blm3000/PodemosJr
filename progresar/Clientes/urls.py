from django.urls import path
from Clientes import views
# urls personales de applicación
urlpatterns = [
    path('clientes/', views.clientes, name = 'clientes'),
    path('grupos/', views.grupos, name = 'grupos'),
    path('clientes/modificarCliente/', views.modificarCliente, name= 'modificarCliente'),
    path('clientes/agregarCliente/', views.agregarCliente, name= 'agregarCliente'),
    path('agregarCaGrupo/<id>',views.agregarCaGrupo, name = 'agregarCaGrupo'),
    path('grupos/guardaGrupoClientes/',views.guardaGrupoClientes, name = 'guardaGrupoClientes'),
    
]
