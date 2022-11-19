from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from parques_nacionales.models import *
from datetime import date
from parques_nacionales.forms import *

contexto_global = {'fecha': date(year=2022,month=11,day=12).strftime("%a %B %d, %Y"),
                'anio' : str(date.today().year),
                'title': 'Explorando Parques Nacionales',
                'title_description':'La Argentina cuenta con 38 Parques Nacionales únicos en el mundo. ',
                
                }

def home(request):

    lista_comentarios = Commentary.objects.all()

    contexto_global['home_url'] = request.get_full_path() == '/home/'
    contexto_global['post_url'] = request.get_full_path() == '/explorando_parques/'
    contexto_global['pagina_actual'] = request.get_full_path()
    contexto_global['lista_comentarios'] = lista_comentarios
    contexto_global['cantidad_comentarios'] = len(lista_comentarios)

    plantilla = loader.get_template('home.html')
    documento = plantilla.render(contexto_global)

    return HttpResponse(documento)

def explorando(request):

    lista_comentarios = Commentary.objects.all()

    contexto_global['home_url'] = request.get_full_path() == '/home/'
    contexto_global['post_url'] = request.get_full_path() == '/explorando_parques/'
    contexto_global['pagina_actual'] = request.get_full_path()
    contexto_global['lista_comentarios'] = lista_comentarios
    contexto_global['cantidad_comentarios'] = len(lista_comentarios)

    plantilla = loader.get_template('post.html')
    documento = plantilla.render(contexto_global)

    return HttpResponse(documento)

def comentarios(request):

    lista_comentarios = Commentary.objects.all()

    contexto_global['home_url'] = request.get_full_path() == '/home/'
    contexto_global['post_url'] = request.get_full_path() == '/explorando_parques/'
    contexto_global['pagina_actual'] = request.get_full_path()
    contexto_global['lista_comentarios'] = lista_comentarios
    contexto_global['cantidad_comentarios'] = len(lista_comentarios)
    contexto_global['script'] = False


    if request.method == 'POST':

        mi_formulario = CommentaryForm(request.POST)
        
        if mi_formulario.is_valid():

            informacion = mi_formulario.cleaned_data
            nuevo_comentario = Commentary(commentarist = informacion['commentarist'],
                                    text_commentary = informacion['text_commentary'],
                                    date_commentary = datetime.now())
            nuevo_comentario.save()
            lista_comentarios = Commentary.objects.all()
            contexto_global['script'] = True

        else:

            errors = mi_formulario.errors 
            contexto_global['errors'] = errors
            
    mi_formulario = CommentaryForm()

    contexto_global['lista_comentarios'] = lista_comentarios
    contexto_global['form'] = mi_formulario
    
    return render(request, 'comentarios.html', contexto_global)

def tags(request):
    


    return redirect(contexto_global['pagina_actual'])
