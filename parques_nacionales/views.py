from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from datetime import date

contexto_global = {'cantidad': 17, 'fecha': date.today().strftime("%a %B %d, %Y"),
                'anio' : str(date.today().year),
                'title_description':'La Argentina cuenta con 38 Parques Nacionales únicos en el mundo. '}

def home(request):

    plantilla = loader.get_template('home.html')
    contexto_global['home_url'] = request.get_full_path() == '/home/'
    documento = plantilla.render(contexto_global)

    return HttpResponse(documento)

def explorando(request):

    plantilla = loader.get_template('post.html')
    contexto_global['home_url'] = request.get_full_path() == '/home/'
    documento = plantilla.render(contexto_global)

    return HttpResponse(documento)
