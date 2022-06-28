from django.urls import path

from .views import *

urlpatterns = [
    # URLS de ProyectoCoderApp
    path('', inicio, name="inicio"),

    path('herramientas/', Herramientas, name="herramientas"),
    path('crear_herramientas/', crear_herramienta, name="crear_herramienta"),
    path('eliminar_herramientas/<herramienta_id>', eliminar_herramienta, name="eliminar_herramienta"),
    path('editar_herramientas/<herramienta_id>', editar_herramientas, name="editar_herramienta"),

    path('herramienta/list', HerramientasList.as_view(), name="herramientas_list"),
    path(r'^(?P<pk>\d+)$', HerramientasDetail.as_view(), name="herramientas_detail"),
    path(r'^nuevo$', HerramientasCreate.as_view(), name="_create"),
    path(r'^editar/(?P<pk>\d+)$', HerramientasUpdate.as_view(), name="herramienta_update"),
    path(r'^eliminar/(?P<pk>\d+)$', HerramientasDelete.as_view(), name="herramienta_delete"),


    
    path('operarios/', operarios, name="operarios"),
    path(r'list', OperarioList.as_view(), name="operario_list"),
    path(r'^(?P<pk>\d+)$', OperarioDetail.as_view(), name="operario_detail"),
    path(r'^nuevo$', OperarioCreate.as_view(), name="operario_create"),
    path(r'^editar/(?P<pk>\d+)$', OperarioUpdate.as_view(), name="operario_update"),
    path(r'^eliminar/(?P<pk>\d+)$', OperarioDelete.as_view(), name="operario_delete"),

    path('maquinas/', maquinas, name="maquinaria"),
    path('crear_maquina/', crear_maquina, name="crear_maquina"),
    path('eliminar_maquina/<maquina_id>/', eliminar_maquina, name="eliminar_maquina"),
    path('editar_maquina/<maquina_id>/', editar_maquina, name="editar_maquina"),
    # path('buscar_comision/', buscar_comision, name="buscar_comision"),
    
    path('entregables/', entregables, name="entregables"),
    # path('base/', base),
]