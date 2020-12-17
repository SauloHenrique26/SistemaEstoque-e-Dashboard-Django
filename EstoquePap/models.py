from django.db import models
from django.contrib.auth.middleware import AuthenticationMiddleware
import EstoquePap.models
from django.contrib.auth.models import UserManager



class NomeMarca (models.Model):
    marcas = models.CharField(max_length=100)
    def __str__(self):
        return self.marcas
    def __str__(self):
        return "%s" % (self.marcas)

class Categoria (models.Model):
    categoria = models.CharField(max_length=100)
    
    def __str__(self):
        return self.categoria

    def __str__(self):
        return "%s" % (self.categoria)




class Itens(models.Model):

    MOVIMENTO=(
        ('e','entrada'),
        ('s','saida'),
        )


    valor = models.DecimalField(max_digits=7, decimal_places=2)
    produto = models.CharField(max_length=300, blank=True, null= True, verbose_name='Nome')
    marca = models.ForeignKey(NomeMarca, models.SET_NULL, blank=True, null=True)    
    categoria= models.ForeignKey(Categoria, models.SET_NULL, blank=True, null=True)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now_add=True)
    movimento = models.CharField (max_length=1, choices=MOVIMENTO, blank=True)
    codigo = models.CharField(max_length=100)
  
   
  

    
    def __str__(self):
        return self.produto

    def __str__(self):
        return "%s" % (self.produto)



    
    # Create your models here.
