from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from parques_nacionales.models import *
from datetime import date

lista_comentarios = Commentary.objects.all()


contexto_global = {'cantidad': 17, 'fecha': date.today().strftime("%a %B %d, %Y"),
                'anio' : str(date.today().year),
                'title': 'Explorando Parques Nacionales',
                'title_description':'La Argentina cuenta con 38 Parques Nacionales únicos en el mundo. ',
                'cantidad_comentarios': len(lista_comentarios),
                }

def home(request):

    contexto_global['home_url'] = request.get_full_path() == '/home/'
    contexto_global['post_url'] = request.get_full_path() == '/explorando_parques/'

    plantilla = loader.get_template('home.html')
    documento = plantilla.render(contexto_global)

    return HttpResponse(documento)

def explorando(request):

    contexto_global['home_url'] = request.get_full_path() == '/home/'
    contexto_global['post_url'] = request.get_full_path() == '/explorando_parques/'

    plantilla = loader.get_template('post.html')
    documento = plantilla.render(contexto_global)

    return HttpResponse(documento)

def comentarios(request):

    contexto_global['home_url'] = request.get_full_path() == '/home/'
    contexto_global['post_url'] = request.get_full_path() == '/explorando_parques/'
    contexto_global['lista_comentarios'] = lista_comentarios

    plantilla = loader.get_template('comentarios.html')
    documento = plantilla.render(contexto_global)

    return HttpResponse(documento)
