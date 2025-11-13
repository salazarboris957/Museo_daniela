from django.shortcuts import render
from .models import Obra, Coleccion

def home(request):
    obras_destacadas = Obra.objects.filter(disponible=True)[:6]
    colecciones = Coleccion.objects.all()
    
    context = {
        'obras_destacadas': obras_destacadas,
        'colecciones': colecciones,
    }
    return render(request, 'galeria/home.html', context)

def galeria_coleccion(request, coleccion_id):
    coleccion = Coleccion.objects.get(id=coleccion_id)
    obras = Obra.objects.filter(coleccion=coleccion, disponible=True)
    
    context = {
        'coleccion': coleccion,
        'obras': obras,
    }
    return render(request, 'galeria/coleccion.html', context)

def obra_detalle(request, obra_id):
    obra = Obra.objects.get(id=obra_id)
    fotos = obra.obrafoto_set.all()
    
    context = {
        'obra': obra,
        'fotos': fotos,
    }
    return render(request, 'galeria/obra_detalle.html', context)