from django.shortcuts import render
from .models import ArticuloBlog

def blog_home(request):
    articulos = ArticuloBlog.objects.all().order_by('-fecha_publicacion')
    return render(request, 'blog/home.html', {'articulos': articulos})

def articulo_detalle(request, articulo_id):
    articulo = ArticuloBlog.objects.get(id=articulo_id)
    return render(request, 'blog/articulo_detalle.html', {'articulo': articulo})