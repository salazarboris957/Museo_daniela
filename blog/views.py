from django.shortcuts import render

def blog_home(request):
    return render(request, 'blog/home.html')

def articulo_detalle(request, articulo_id):
    return render(request, 'blog/articulo_detalle.html', {})
