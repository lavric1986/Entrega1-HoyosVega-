import datetime

from django.shortcuts import redirect, render
from django.http import HttpResponse

from .models import Maquinaria, Herramientas, Operario
from .forms import HerramientaFormulario, NuevaMaquina
from django.db.models import Q

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from django.urls import reverse_lazy

# Create your views here.

def inicio(request):

    nombre = "Juan"
    hoy = datetime.datetime.now()
    notas = [4,9,7,8,5,10]

    return render(request,"ProyectoCoderApp/index.html",{"mi_nombre":nombre,"dia_hora":hoy,"notas":notas})

"""
def buscar_comision(request):

    if request.method == "POST":

        comision = request.POST["comision"]
        
        comisiones = Curso.objects.filter( Q(nombre__icontains=comision) | Q(comision__icontains=comision) ).values()
        # User.objects.filter(Q(income__gte=5000) | Q(income__isnull=True))

        return render(request,"ProyectoCoderApp/buscar_comision.html",{"comisiones":comisiones})

    else: # get y otros

        comisiones =  []  #Curso.objects.all()
        
        return render(request,"ProyectoCoderApp/buscar_comision.html",{"comisiones":comisiones})
"""

def herramientas(request):

    if request.method == "POST":

        search = request.POST["search"]

        if search != "":
            herramientas = Herramientas.objects.filter( Q(tipo__icontains=search) | Q(marca__icontains=search)|Q(codigo_icontains=search) ).values()

            return render(request,"ProyectoCoderApp/herramientas.html",{"herramientas":herramientas, "search":True, "busqueda":search})

    herramientas = Herramientas.objects.all()

    return render(request,"ProyectoCoderApp/herramientas.html",{"herramientas":herramientas})

def crear_herramienta(request):
    
    # post
    if request.method == "POST":
        
        formulario = HerramientaFormulario(request.POST)

        if formulario.is_valid():
            
            info = formulario.cleaned_data

            herramienta = Herramientas(tipo=info["tipo"],marca=info["marca"],codigo=info["codigo"])
            herramienta.save()

            return redirect("herramientas")

        return render(request,"ProyectoCoderApp/formulario_herramienta.html",{"form":formulario})

    # get
    formulario = HerramientaFormulario()
    return render(request,"ProyectoCoderApp/formulario_herramienta.html",{"form":formulario})

def eliminar_herramienta(request,herramienta_id):

    herramienta = Herramientas.objects.get(id = herramienta_id)
    herramienta.delete()

    return redirect("herramientas")

def editar_herramientas(request,herramienta_id):

    herramienta = Herramientas.objects.get(id = herramienta_id)

    if request.method == "POST":

        formulario = HerramientaFormulario(request.POST)

        if formulario.is_valid():
            
            info_herramienta = formulario.cleaned_data
            
            herramienta.tipo = info_herramienta["tipo"]
            herramienta.marca = info_herramienta["marca"]
            herramienta.codigo = info_herramienta["codigo"]
            herramienta.save()

            return redirect("herramientas")

    # get
    formulario = HerramientaFormulario(initial={"tipo":herramienta.tipo, "marca":herramienta.marca, "codigo": herramienta.codigo})
    
    return render(request,"ProyectoCoderApp/formulario_herramienta.html",{"form":formulario})

class HerramientasList(ListView):

    model = Herramientas
    template_name = "ProyectoCoderApp/herramientas_list.html"

class HerramientasDetail(DetailView):

    model = Herramientas
    template_name = "ProyectoCoderApp/herramientas_detail.html"

class HerramientasCreate(CreateView):

    model = Herramientas
    success_url = "/coderapp/herramientas/list" # atenciooooooooon!!!! a la primer /
    fields = ["tipo", "marca", "codigo"]

class HerramientasUpdate(UpdateView):

    model = Herramientas
    success_url = "/coderapp/herramientas/list" # atenciooooooooon!!!! a la primer /
    fields = ["tipo", "marca", "codigo"]

class HerramientasDelete(DeleteView):

    model = Herramientas
    success_url = "/coderapp/herramientas/list" # atenciooooooooon!!!! a la primer /


def maquinas(request):

    if request.method == "POST":

        search = request.POST["search"]

        if search != "":
            maquinaria = Maquinaria.objects.filter( Q(marca__icontains=search) | Q(funcion__icontains=search) ).values()

            return render(request,"ProyectoCoderApp/maquinaria.html",{"maquinaria": maquinaria , "search":True, "busqueda":search})

    maquinaria = Maquinaria.objects.all()

    return render(request,"ProyectoCoderApp/maquinaria.html",{"maquinaria":maquinaria, "search":False})

def crear_maquina(request):

    # post
    if request.method == "POST":

        formulario = NuevaMaquina(request.POST)

        if formulario.is_valid():

            info_maquinaria = formulario.cleaned_data
        
            maquinaria = Maquinaria(marca=info_maquinaria["marca"], funcion=info_maquinaria["funcion"])
            maquinaria.save() # guardamos en la bd
            
            return redirect("maquinaria")

        else:

            return render(request,"ProyectoCoderApp/formulario_curso.html",{"form":formulario,"accion":"Crear Curso"})
    

    else: # get y otros

        formularioVacio = NuevaMaquina()

        return render(request,"ProyectoCoderApp/formulario_maquinaria.html",{"form":formularioVacio,"accion":"Crear Maquina"})

def eliminar_maquina(request, maquinaria_id):

    # post
    maquinaria = Maquinaria.objects.get(id=maquinaria_id)
    maquinaria.delete()

    return redirect("maquinaria")

def editar_maquina(request, maquinaria_id):

    # post
    
    maquinaria = Maquinaria.objects.get(id=maquinaria_id)

    if request.method == "POST":

        formulario = NuevaMaquina(request.POST)

        if formulario.is_valid():

            info_maquinaria = formulario.cleaned_data
        
            maquinaria.marca = info_maquinaria["marca"]
            maquinaria.funcion = info_maquinaria["funcion"]
            maquinaria.save() # guardamos en la bd
            
            return redirect("maquinaria")

            
    formulario = NuevaMaquina(initial={"marca":maquinaria.marca,"funcion":maquinaria.funcion})

    return render(request,"ProyectoCoderApp/formulario_maquinaria.html",{"form":formulario,"accion":"Editar Maquina"})


def operarios(request):

    operarios = Operario.objects.all()

    return render(request,"ProyectoCoderApp/operarios.html",{"operarios":operarios})

class OperarioList(ListView):

    model = Operario
    template_name = "ProyectoCoderApp/operarios_list.html"


class OperarioDetail(DetailView):

    model = Operario
    template_name = "ProyectoCoderApp/operarios_detail.html"


class OperarioCreate(CreateView):

    model = Operario
    success_url = "/coderapp/list"#reverse_lazy("profes_list")
    fields = ["nombre", "apellido", "email", "profesion"]

class OperarioUpdate(UpdateView):

    model = Operario
    success_url = "/coderapp/list"#reverse_lazy("profes_list")
    fields = ["nombre", "apellido", "email", "profesion"]

class OperarioDelete(DeleteView):

    model = Operario
    success_url = "/coderapp/list"#reverse_lazy("profes_list")

def base(request):
    return render(request,"ProyectoCoderApp/base.html",{})

def entregables(request):
    return HttpResponse("Vista de entregables")