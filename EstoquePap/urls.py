from django.conf.urls import include, url
import django
import EstoquePap.views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings




#app_name = 'EstoquePap'

urlpatterns = [
    path('index/',EstoquePap.views.index, name='index'),
    url(r'^home/', EstoquePap.views.index, name='home'),
   url(r'^dashboard$', EstoquePap.views.dashboard, name='dashboard'),
    path('tabela_itens',EstoquePap.views.tabela_itens, name='tabela_itens'),
    url(r'^adicionar_marca$',EstoquePap.views.adicionarmarca, name='adicionarmarca'),
    url(r'^adicionar_categoria$', EstoquePap.views.adicionarcategoria, name='adicionarcategoria'),
    path('edit/<int:id>', EstoquePap.views.editItem, name='edit_item'),
    path('delete/<int:id>', EstoquePap.views.deleteItem, name='delete_item'),
    #path('saida/<int:id>', EstoquePap.views.saidaitem, name='saidaitem'),

   

    #url(r'^$',)
   ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
