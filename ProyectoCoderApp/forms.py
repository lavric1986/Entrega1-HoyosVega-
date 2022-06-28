from django import forms


class NuevaMaquina(forms.Form):

    marca = forms.CharField(max_length=30,label="Maquinaria")
    funcion = forms.CharField(max_length=30)

class HerramientaFormulario(forms.Form):

    tipo = forms.CharField(max_length=30)
    marca = forms.CharField(max_length=30)

    codigo = forms.IntegerField()