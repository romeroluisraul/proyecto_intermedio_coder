from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def home(request):

    plantilla = loader.get_template('home.html')
    documento = plantilla.render()

    return HttpResponse(documento)

def explorando(request):

    plantilla = loader.get_template('base.html')
    documento = plantilla.render()

    return HttpResponse(documento)
