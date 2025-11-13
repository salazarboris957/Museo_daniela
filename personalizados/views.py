from django.shortcuts import render

def personalizados_home(request):
    return render(request, 'personalizados/home.html')

def solicitar_personalizado(request):
    return render(request, 'personalizados/solicitar.html', {})

def personalizados_gracias(request):
    return render(request, 'personalizados/gracias.html', {})
