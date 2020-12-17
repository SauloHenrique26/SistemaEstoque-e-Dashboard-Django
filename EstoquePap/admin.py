from django.contrib import admin
import EstoquePap.models
from .models import NomeMarca, Itens, Categoria 



admin.site.register(Itens)
admin.site.register(NomeMarca)
admin.site.register(Categoria)



# Register your models here.
