from django import forms
from .models import Itens, Categoria, NomeMarca

class Itensform (forms.ModelForm):


    class Meta:
        model = Itens
        fields = ('produto','valor','marca','categoria','codigo')




class Categoriaform(forms.ModelForm):
    class Meta:
         model =  Categoria
         fields =('categoria',)

class Marcaform(forms.ModelForm):
    class Meta:
         model = NomeMarca
         fields =('marcas',)

class Saidaform(forms.ModelForm):
    class Meta:
         model =  Itens
         fields =('codigo',)