from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from parques_nacionales.models import *
from datetime import date
from parques_nacionales.forms import *
from django.db.models import Q

contexto_global = {'fecha': date(year=2022,month=11,day=12).strftime("%a %B %d, %Y"),
                'anio' : str(date.today().year),
                'title': 'Explorando Parques Nacionales',
                'title_description':'La Argentina cuenta con 38 Parques Nacionales únicos en el mundo. ',
                
                }

def home(request):

    lista_comentarios = Commentary.objects.all()

    contexto_global['home_url'] = request.get_full_path() == '/home/'
    contexto_global['post_url'] = request.get_full_path() == '/explorando_parques/'
    contexto_global['lista_comentarios'] = lista_comentarios
    contexto_global['cantidad_comentarios'] = len(lista_comentarios)

    plantilla = loader.get_template('home.html')
    documento = plantilla.render(contexto_global)

    return HttpResponse(documento)

def explorando(request):

    lista_comentarios = Commentary.objects.all()

    contexto_global['home_url'] = request.get_full_path() == '/home/'
    contexto_global['post_url'] = request.get_full_path() == '/explorando_parques/'
    contexto_global['lista_comentarios'] = lista_comentarios
    contexto_global['cantidad_comentarios'] = len(lista_comentarios)

    plantilla = loader.get_template('post.html')
    documento = plantilla.render(contexto_global)

    return HttpResponse(documento)

def comentarios(request):

    lista_comentarios = Commentary.objects.all()

    contexto_global['home_url'] = request.get_full_path() == '/home/'
    contexto_global['post_url'] = request.get_full_path() == '/explorando_parques/'
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

def tags(request, tag):


    lista_comentarios = Commentary.objects.all()

    contexto_global['home_url'] = request.get_full_path() == '/home/'
    contexto_global['post_url'] = request.get_full_path() == '/explorando_parques/'
    contexto_global['lista_comentarios'] = lista_comentarios
    contexto_global['cantidad_comentarios'] = len(lista_comentarios)
    contexto_global['script'] = False

    etiqueta = tag
    posts = Post.objects.filter(Q(tag1__icontains=etiqueta) | Q(tag2__icontains=etiqueta))

    def choices(tag):

        TRAVEL,AR,CL = 'TR','AR','CL'
        CUYO, PATAGONIA, COSTA, BUENOS_AIRES, CENTRO = 'CY','PAT','MDP','BSAS','COB'
        PARQUES, LAGOS, RUTAS, MONTANIAS = 'PN','LG','RN','MNT'
        IDEAS, RATA_TIPS = 'ID','TIP'

        TAGS_CHOICES = [(TRAVEL, 'Travel'),
                        (AR, 'Argentina'), (CL, 'Chile'),
                        (CUYO, 'Cuyo'), (PATAGONIA, 'Patagonia'), (COSTA, 'Costa Atlántica'),
                        (BUENOS_AIRES, 'Buenos Aires'), (CENTRO, 'Centro'),
                        (PARQUES, 'Parques'), (LAGOS, 'Lagos'), (RUTAS, 'Rutas'), (MONTANIAS, 'Montañas'),
                        (IDEAS, 'Ideas'), (RATA_TIPS, 'Rata-tips')]

        i = 0
        while TAGS_CHOICES[i][0] != tag.upper():
            i += 1

        return(TAGS_CHOICES[i][1])

    contexto_global['tag_buscado'] = choices(etiqueta)
    contexto_global['posts'] = posts

    return render(request, 'resultados.html', contexto_global)
