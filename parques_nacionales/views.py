from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from parques_nacionales.models import *
from parques_nacionales.forms import *
from django.db.models import Q
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

from datetime import date
from time import sleep



contexto_global = {'anio' : str(date.today().year),
                   'title': 'Explorando Parques Nacionales',
                   'title_description': 'La Argentina cuenta con 38 Parques Nacionales únicos en el mundo. ',
                   'fecha': date(2022,11,9)}

def home(request):

    lista_comentarios = Commentary.objects.all()

    contexto_global['home_url'] = request.get_full_path() == '/home/'
    contexto_global['post_url'] = request.get_full_path() == '/explorando_parques/'
    contexto_global['pagina_actual'] = request.get_full_path()
    contexto_global['lista_comentarios'] = lista_comentarios
    contexto_global['cantidad_comentarios'] = len(lista_comentarios)

    post_second = Post.objects.get(title__icontains = 'salimos?')
    contexto_global['post_snd'] = post_second

    return render(request, 'home.html', contexto_global)

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
            nuevo_comentario = Commentary(commentarist = request.user,
                                    text_commentary = informacion['text_commentary'],
                                    date_commentary = datetime.now())
            nuevo_comentario.save()
            lista_comentarios = Commentary.objects.all()
            contexto_global['script'] = True

        else:

            errors = mi_formulario.errors 
            contexto_global['errors'] = errors
            print(errors)
            
    mi_formulario = CommentaryForm()

    contexto_global['lista_comentarios'] = lista_comentarios
    contexto_global['form'] = mi_formulario
    
    return render(request, 'comentarios.html', contexto_global)

def tags(request, tag):


    lista_comentarios = Commentary.objects.all()

    contexto_global['home_url'] = request.get_full_path() == '/home/'
    contexto_global['post_url'] = request.get_full_path() == '/explorando_parques/'
    contexto_global['pagina_actual'] = request.get_full_path()
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

def logeo_user(request):

    contexto_global['home_url'] = request.get_full_path() == '/home/'
    contexto_global['post_url'] = request.get_full_path() == '/explorando_parques/'

    if request.method == 'POST':

        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():

            print(type(form.cleaned_data))

            usuario = form.cleaned_data['username']
            contra = form.cleaned_data['password']

            user = authenticate(username=usuario, password = contra)

            if user is not None:

                login(request, user)
                contexto_global['contador'] = 0
                respuesta = redirect('bienvenida')

            else:
                errores = form.errors
                contexto_global['errores_acceso'] = errores
                respuesta = render(request, 'acceso_usuarios.html', contexto_global)
                print(errores)
        else:
            errores = form.errors
            contexto_global['errores_acceso'] = errores
            respuesta = render(request, 'acceso_usuarios.html', contexto_global)

    if request.method == 'GET':

        contexto_global['errores_acceso'] = False
        contexto_global['form_usuarios'] = True
        respuesta = render(request, 'acceso_usuarios.html', contexto_global)
    
    form = AuthenticationForm()

    return respuesta

@login_required
def bienvenida(request):

    if contexto_global['contador'] == 0:

        contexto_global['contador'] += 1
        respuesta = render(request, 'bienvenida.html', contexto_global)

    else:
        sleep(2)
        respuesta = redirect(contexto_global['pagina_actual'])

    return respuesta

@login_required
def deslogeo_user(request, destino = ''):
    
    logout(request)

    if destino != '':

        respuesta = redirect(destino)

    else:

        respuesta = redirect(contexto_global['pagina_actual'])

    return respuesta
