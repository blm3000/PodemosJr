from django.contrib import admin
from .models import Cliente,Grupo

# Register your models here.
class ClienteAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")


class GrupoAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")


admin.site.register(Cliente,ClienteAdmin)
admin.site.register(Grupo,GrupoAdmin)