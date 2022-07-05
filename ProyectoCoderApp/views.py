import datetime

from django.shortcuts import redirect, render
from django.http import HttpResponse

from .models import Maquinaria, Herramientas, Operario
from .forms import HerramientaFormulario, NuevaMaquina, NuevoOperario
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

def herramientas(request):

    if request.method == "POST":

        search = request.POST["search"]

        if search != "":
            herramientas = Herramientas.objects.filter( Q(tipo__icontains=search) | Q(marca__icontains=search)).values()

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

def eliminar_herramienta(request,herramientas_id):

    herramientas = Herramientas.objects.get(id = herramientas_id)
    herramientas.delete()

    return redirect("herramientas")

def editar_herramientas(request,herramientas_id):

    herramientas = Herramientas.objects.get(id = herramientas_id)

    if request.method == "POST":

        formulario = HerramientaFormulario(request.POST)

        if formulario.is_valid():
            
            info_herramienta = formulario.cleaned_data
            
            herramientas.tipo = info_herramienta["tipo"]
            herramientas.marca = info_herramienta["marca"]
            herramientas.codigo = info_herramienta["codigo"]
            herramientas.save()

            return redirect("herramientas")

    # get
    formulario = HerramientaFormulario(initial={"tipo":herramientas.tipo, "marca":herramientas.marca, "codigo": herramientas.codigo})
    
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
            maquinas = Maquinaria.objects.filter( Q(marca__icontains=search) | Q(funcion__icontains=search) ).values()

            return render(request,"ProyectoCoderApp/maquinaria.html",{"maquinas": maquinas , "search":True, "busqueda":search})

    maquinas = Maquinaria.objects.all()

    return render(request,"ProyectoCoderApp/maquinaria.html",{"maquinas":maquinas, "search":False})

def crear_maquina(request):

    # post
    if request.method == "POST":

        formulario = NuevaMaquina(request.POST)

        if formulario.is_valid():

            info_maquinaria = formulario.cleaned_data
        
            maquinas = Maquinaria(marca=info_maquinaria["marca"], funcion=info_maquinaria["funcion"])
            maquinas.save() # guardamos en la bd
            
            return redirect("maquinas")

        return render(request,"ProyectoCoderApp/formulario_maquinaria.html",{"form":formulario,"accion":"crear maquina"})
    

    # get y otros

    formularioVacio = NuevaMaquina()

    return render(request,"ProyectoCoderApp/formulario_maquinaria.html",{"form":formularioVacio,"accion":"crear Maquina"})

def eliminar_maquina(request, maquina_id):

    # post
    maquinas = Maquinaria.objects.get(id = maquina_id)
    maquinas.delete()

    return redirect("maquinas")

def editar_maquina(request, maquina_id):

    # post
    
    maquinas = Maquinaria.objects.get(id = maquina_id)

    if request.method == "POST":

        formulario = NuevaMaquina(request.POST)

        if formulario.is_valid():

            info_maquinaria = formulario.cleaned_data
        
            maquinas.marca = info_maquinaria["marca"]
            maquinas.funcion = info_maquinaria["funcion"]
            maquinas.save() # guardamos en la bd
            
            return redirect("maquinas")

            
    formulario = NuevaMaquina(initial={"marca":maquinas.marca,"funcion":maquinas.funcion})

    return render(request,"ProyectoCoderApp/formulario_maquinaria.html",{"form":formulario,"accion":"Editar Maquina"})


def operarios(request):
     if request.method == "POST":

        search = request.POST["search"]

        if search != "":
            operarios = Operario.objects.filter( Q(nombre__icontains=search) | Q(apellido__icontains=search) ).values()

            return render(request,"ProyectoCoderApp/operarios.html",{"operarios": operarios , "search":True, "busqueda":search})

     operarios = Operario.objects.all()

     return render(request,"ProyectoCoderApp/operarios.html",{"operarios":operarios, "search":False})

def crear_operarios(request):
     if request.method == "POST":
        
        formulario = NuevoOperario(request.POST)

        if formulario.is_valid():
            
            info = formulario.cleaned_data

            operario = Operario(nombre=info["nombre"],apellido=info["apellido"],area=info["area"])
            operario.save()

            return redirect("operarios")

        return render(request,"ProyectoCoderApp/operarios_formulario.html",{"form":formulario})

    # get
     formulario = NuevoOperario()
     return render(request,"ProyectoCoderApp/operarios_formulario.html",{"form":formulario})

def eliminar_operarios(request,operario_id):
    operario = Operario.objects.get(id=operario_id )
    operario.delete()

    return redirect("operarios")

def editar_operarios(request,operario_id):
    operario = Operario.objects.get(id = operario_id)

    if request.method == "POST":

        formulario = NuevoOperario(request.POST)

        if formulario.is_valid():
            
            info_operarios = formulario.cleaned_data
            
            operario.tipo = info_operarios["nombre"]
            operario.marca = info_operarios["apellido"]
            operario.codigo = info_operarios["area"]
            operario.save()

            return redirect("operarios")

    # get
    formulario = NuevoOperario(initial={"nombre":operario.nombre, "apellido":operario.apellido, "area": operario.area})
    
    return render(request,"ProyectoCoderApp/operarios_formulario.html",{"form":formulario})

    # return render(request,"ProyectoCoderApp/operarios.html",{"operarios":operarios})

# class OperarioList(ListView):

#     model = Operario
#     template_name = "ProyectoCoderApp/operarios_list.html"


# class OperarioDetail(DetailView):

#     model = Operario
#     template_name = "ProyectoCoderApp/operarios_detail.html"


# class OperarioCreate(CreateView):

#     model = Operario
#     success_url = "/coderapp/list"#reverse_lazy("operarios_list")
#     fields = ["nombre", "apellido", "area"]

# class OperarioUpdate(UpdateView):

#     model = Operario
#     success_url = "/coderapp/list"#reverse_lazy("operarios_list")
#     fields = ["nombre", "apellido", "area"]

# class OperarioDelete(DeleteView):

#     model = Operario
#     success_url = "/coderapp/list"#reverse_lazy("operarios_list")

def base(request):
    return render(request,"ProyectoCoderApp/base.html",{})

def entregables(request):
    return HttpResponse("Vista de entregables")