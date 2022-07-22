import datetime

from django.shortcuts import redirect, render
from django.http import HttpResponse

from .models import Avatar, Maquinaria, Herramientas, Operario
from .forms import HerramientaFormulario, NuevaMaquina, NuevoOperario
from django.db.models import Q

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm #, UserCreationForm
from .forms import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.core.files.storage import FileSystemStorage
# Create your views here.

def inicio(request):
    

    nombre = "Juan"
    hoy = datetime.datetime.now()
    notas = [4,9,7,8,5,10]
    
    if request.user.is_authenticated:
        try:
            avatar=Avatar.objects.get(usuario=request.user)
            url = avatar.imagen.url
        except:
            url="/media/avatar/Profile"
        return render(request,"ProyectoCoderApp/index.html",{"mi_nombre":nombre,"dia_hora":hoy,"notas":notas,"url":url})

    return render(request,"ProyectoCoderApp/index.html",{"mi_nombre":nombre,"dia_hora":hoy,"notas":notas,})
    


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            
            if user is not None:
                login(request, user)
                return redirect("inicio")
            else:
                return redirect("login")
            
        else:
            return redirect("login")
    
    form=AuthenticationForm()
            
    return render(request,"ProyectoCoderApp/login.html", {"form":form})
def register_request(request):
     if request.method == "POST":
         form= UserRegisterForm(request.POST)
         #form= UserCreationForm(request.POST)
         
         if form.is_valid():
             
             username =form.cleaned_data.get('username')
             password =form.cleaned_data.get('password1')# es la primer contraseña no la confirmacion 
            
             
             form.save()#registramos el usuario
             user= authenticate(username=username,password=password)
             
             return redirect("login")
         
         return render(request,"ProyectoCoderApp/register.html",{"form":form})
    
     
         
     form =UserRegisterForm ()
    
     return render(request,"ProyectoCoderApp/register.html",{"form":form})

def logout_request(request):
    logout(request)
    return redirect('inicio')

@login_required
def editar_perfil(request):
    
    user=request.user #usuario con el que estoy logeado
    
    if request.method == "POST":
        form = UserEditForm(request.POST)
        
        if form.is_valid():
            info =form.cleaned_data
            user.email = info["email"]
            user.first_name = info["first_name"]
            user.last_name = info["last_name"]
            
            user.save()
            
            return redirect("inicio")
    
    else:
        form =UserEditForm(initial={"email":user.email,"first_name":user.first_name,"last_name":user.last_name})
    return render(request,"ProyectoCoderApp/editar_perfil.html",{"form":form})
@login_required
def agregar_avatar(request):
    if request.method == 'POST':
        form =AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            user=User.objects.get(username=request.user.username)
            
            avatar = Avatar (usuario=user, imagen=form.cleaned_data['imagen'])
            avatar.save()
            
            # return render(request, "ProyectoCoderApp/index.html")
            return redirect('inicio')
    else:
        form=AvatarForm()
    
    return render(request,"ProyectoCoderApp/agregar_avatar.html",{"form":form})


    
    

def herramientas(request):

    if request.method == "POST":

        search = request.POST["search"]

        if search != "":
            herramientas = Herramientas.objects.filter( Q(tipo__icontains=search) | Q(marca__icontains=search)).values()

            return render(request,"ProyectoCoderApp/herramientas.html",{"herramientas":herramientas, "search":True, "busqueda":search})

    herramientas = Herramientas.objects.all()

    return render(request,"ProyectoCoderApp/herramientas.html",{"herramientas":herramientas})

@staff_member_required
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

@staff_member_required
def eliminar_herramienta(request,herramientas_id):

    herramientas = Herramientas.objects.get(id = herramientas_id)
    herramientas.delete()

    return redirect("herramientas")

@staff_member_required
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

@login_required
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

@login_required
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

class OperarioList(LoginRequiredMixin,ListView):

    model = Operario
    template_name = "ProyectoCoderApp/operarios_list.html"


class OperarioDetail(DetailView):

    model = Operario
    template_name = "ProyectoCoderApp/operarios_detail.html"


class OperarioCreate(CreateView):

    model = Operario
    success_url = "/coderapp/list"#reverse_lazy("operarios_list")
    fields = ["nombre", "apellido", "area"]

class OperarioUpdate(UpdateView):

    model = Operario
    success_url = "/coderapp/list"#reverse_lazy("operarios_list")
    fields = ["nombre", "apellido", "area"]

class OperarioDelete(DeleteView):

    model = Operario
    success_url = "/coderapp/list"#reverse_lazy("operarios_list")

def base(request):
    return render(request,"ProyectoCoderApp/base.html",{})

def entregables(request):
    
    return HttpResponse("Vista de entregables")

