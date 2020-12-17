"""
Definition of urls for ProjetoEstoque.
"""

from django.conf.urls import include, url
import EstoquePap.urls
import EstoquePap.views
from django.conf import Path
from django.contrib import admin
from django.urls import path

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
   url('admin/', admin.site.urls),
    url('', include('EstoquePap.urls')),
    url(r'^$',EstoquePap.views.index, name='index'),
 
   #url(r'^dashboard$', EstoquePap.views.dashboard, name='dashboard'),
    
    #url(r'^home$', EstoquePap.views.index, name='home')
]
