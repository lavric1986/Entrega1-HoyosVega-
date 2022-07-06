from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
class NuevoOperario(forms.Form):
    nombre= forms.CharField(max_length=30)
    apellido=forms.CharField(max_length=30)
    area=forms.CharField(max_length=30)

class NuevaMaquina(forms.Form):

    marca = forms.CharField(max_length=30,label="Maquinaria")
    funcion = forms.CharField(max_length=30)

class HerramientaFormulario(forms.Form):

    tipo = forms.CharField(max_length=30)
    marca = forms.CharField(max_length=30)
    codigo = forms.IntegerField()

class UserRegisterForm(UserCreationForm):
    email=forms.EmailField(label='Email')
    password1=forms.CharField(label="contraseña", widget=forms.PasswordInput)
    password2=forms.CharField(label="confirmar contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model= User
        fields=['username',"email","password1","password2"]
        
        help_text={k:"" for k in fields}