from django.shortcuts import render, redirect, get_object_or_404
from django.conf.urls import include, url
import EstoquePap
from EstoquePap.models import Itens,NomeMarca,Categoria 
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.db import connection
from .forms import Itensform,Marcaform, Categoriaform, Saidaform
from django.contrib import messages
from django.db.models import Avg, Count, Min, Sum
import datetime
import json
from django.http import JsonResponse
#import highcharts
from django.db.models.functions import Extract

# Create your views here.


    

def index (request):
   if request.method =='POST':
        form = Itensform(request.POST)         
        if form.is_valid() and 'btnentrada' in request.POST:           
            produto = Itens.objects.all()            
            add = form.save(commit=False)
            add.movimento = 'e'
            add.save()  
        elif form.is_valid() and 'btnsaida' in request.POST:                      
            add1 = form.save(commit=False)
            produto = Itens.objects.get(codigo__contains = add1.codigo)
            if add1.codigo == produto.codigo:              
                produto = Itens.objects.filter(codigo__contains = add1.codigo).update(movimento='s')
                 
        form_item =  Itensform()
        return render(request, 'EstoquePap/index.html', {'form': form_item} )
        

   
   else:
        form_item =  Itensform()
      
        
        return render(request, 'EstoquePap/index.html', {'form': form_item} )

def saidaitem(request,id):
    if request.method =='POST':
        form = Saidaform(request.POST)
        if form.is_valid():
            add1 = form.save(commit=False)
            produto = Itens.objects.get(codigo__contains = add1.codigo)

        
    

def editItem(request, id):
    produto= get_object_or_404(Itens, pk=id)
    form=Itensform(instance=produto)
    if(request.method == 'POST'):
        form=Itensform(request.POST, instance=produto)
        if(form.is_valid()):
            form.save()
            return redirect('tabela_itens')
    else:
        return render (request, 'EstoquePap/editItem.html', {'form': form})

def deleteItem(request, id):
    produto= get_object_or_404(Itens, pk=id)
    produto.delete()

    messages.info(request, 'Item Deletado com sucesso!')
    return redirect('tabela_itens')
    


def dashboard(request):
    
    #contador de itens
    TotalItem=Itens.objects.filter(movimento='e').count()
    
    #total de valor
    Totalvalor=Itens.objects.filter(movimento='e').aggregate(Sum('valor'))['valor__sum'] or 0.00
    totval=round(Totalvalor, 2)

    #saidas recentes
    saidasrecentes = Itens.objects.filter(movimento='s', updated_at__gt=datetime.datetime.now()-datetime.timedelta(days=7)).count()

    #entrada mês
    totalem=Itens.objects.filter(movimento='e', updated_at__gt=datetime.datetime.now()-datetime.timedelta(days=30)).count()

    #saida mês
    totalsm=Itens.objects.filter(movimento='s', updated_at__gt=datetime.datetime.now()-datetime.timedelta(days=30)).count()

    #total de marcas cadastradas
    totaldemarcas= NomeMarca.objects.all().count()

    #testdata
    #a=Itens.objects.values('updated_at').ExtractMonth()
    #grafico 1
    dataset = Itens.objects \
        .values() \
        .annotate(survived_count=Count('produto',movimento='e'),
                  not_survived_count=Count('produto',movimento='s')) \
        .order_by('updated_at')

    categories = list()
    survived_series_data = list()
    not_survived_series_data = list()

    for entry in dataset:
        categories.append('%s Class' % entry['updated_at'])
        survived_series_data.append(entry['survived_count'])
        not_survived_series_data.append(entry['not_survived_count'])

    survived_series = {
        'name': 'Entada',
        'data': survived_series_data,
        'color': 'green'
    }

    not_survived_series = {
        'name': 'Saida',
        'data': not_survived_series_data,
        'color': 'red'
    }

    chart = {
        'chart': {'type': 'column'},
        'title': {'text': 'Titanic Survivors by Ticket Class'},
        'xAxis': {'categories': categories},
        'series': [survived_series, not_survived_series]
    }

    dump = json.dumps(chart)
        
    
    


    return render (

        request,'EstoquePap/Dashboard.html',
        {'total':TotalItem, 'totavalor':totval, 'saida7d':saidasrecentes, 'marcastotal':totaldemarcas, 'dataset':dataset, 'chart': dump}

        )

def tabela_itens(request):
    produto = Itens.objects.all()
    
      
    return render (request,'EstoquePap/ItensnoEstoque.html', {'EstoquePap': produto})


def adicionarmarca(request):
    if request.method =='POST':
        form = Marcaform(request.POST)
        add = form.save(commit=False)
        add.save() 
        form_marca =  Marcaform()
        return render(request, 'EstoquePap/AdicionarMarca.html', {'form':  form_marca} )
    else:
        form_marca =  Marcaform()
        return render(request, 'EstoquePap/AdicionarMarca.html', {'form':  form_marca} )

def adicionarcategoria(request):
    if request.method =='POST':
        form = Categoriaform(request.POST)
        add = form.save(commit=False)
        add.save() 
        form_categoria =  Categoriaform()
        return render(request, 'EstoquePap/AdicionarCategoria.html', {'form':  form_categoria} )
    else:
        form_categoria =  Categoriaform()
        return render(request, 'EstoquePap/AdicionarCategoria.html', {'form':  form_categoria} )


    
         