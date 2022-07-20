from django.contrib import admin

from .models import *

# Register your models here.

class MaquinasAdmin(admin.ModelAdmin):

    list_display = ('marca','funcion')
    search_fields = ('marca', 'funcion')


class HerramientaAdmin(admin.ModelAdmin):

    list_display = ('tipo', 'marca', 'codigo')


class OperarioAdmin(admin.ModelAdmin):

    list_display = ('nombre', 'apellido', 'area')
    


# class EntregableAdmin(admin.ModelAdmin):

#     list_display = ('nombre', 'fechaEntrega', 'entregado')


admin.site.register(Maquinaria,MaquinasAdmin)
admin.site.register(Herramientas, HerramientaAdmin)
admin.site.register(Operario,OperarioAdmin)
admin.site.register(Entregable) # , EntregableAdmin

# admin, admin -> python manage.py createsuperuser
admin.site.register(Avatar)