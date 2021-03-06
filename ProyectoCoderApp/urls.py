from django.urls import path

from .views import *

urlpatterns = [
    # URLS de ProyectoCoderApp
    path('', inicio, name="inicio"),
    path('login/', login_request, name="login"),#no usar login como nombre de la vista
    path('register/', register_request, name="register"),
    path('logout/', logout_request, name="logout"),
    path('editar_perfil/', editar_perfil, name="editar_perfil"),
    path('agregar_avatar', agregar_avatar, name="agregar_avatar"),
    
  
   
    

    path('herramientas/', herramientas , name= "herramientas"),
    path('crear_herramientas/', crear_herramienta, name="crear_herramientas"),
    path('eliminar_herramientas/<herramientas_id>', eliminar_herramienta, name="eliminar_herramientas"),
    path('editar_herramientas/<herramientas_id>', editar_herramientas, name="editar_herramientas"),

    path('herramientas/list', HerramientasList.as_view(), name="herramientas_list"),
    path(r'^(?P<pk>\d+)$', HerramientasDetail.as_view(), name="herramientas_detail"),
    path(r'^nuevo$', HerramientasCreate.as_view(), name="herramientas_create"),
    path(r'^editar/(?P<pk>\d+)$', HerramientasUpdate.as_view(), name="herramientas_update"),
    path(r'^eliminar/(?P<pk>\d+)$', HerramientasDelete.as_view(), name="herramientas_delete"),


    
    path('operarios/', operarios, name="operarios"),
    path('crear_operarios/', crear_operarios, name="crear_operarios"),
    path('eliminar_operarios/<operario_id>', eliminar_operarios, name="eliminar_operarios"),
    path('editar_operarios/<operario_id>', editar_operarios, name="editar_operarios"),
    
    
    
    
    
    path('operarios/list', OperarioList.as_view(), name="operarios_list"),
    path('operarios/<pk>', OperarioDetail.as_view(), name="operarios_detail"),
    path('operarios/nuevo', OperarioCreate.as_view(), name="operario_create"),
    path('operarios/editar/<pk>', OperarioUpdate.as_view(), name="operario_update"),
    path('operarios/eliminar/<pk>', OperarioDelete.as_view(), name="operario_delete"),

    path('maquinas/', maquinas, name= "maquinas"),
    path('crear_maquina/', crear_maquina, name="crear_maquina"),
    path('eliminar_maquina/<maquina_id>/', eliminar_maquina, name="eliminar_maquina"),
    path('editar_maquina/<maquina_id>/', editar_maquina, name="editar_maquina"),
    # path('buscar_comision/', buscar_comision, name="buscar_comision"),
    
    path('entregables/', entregables, name="entregables"),
    # path('base/', base),
]