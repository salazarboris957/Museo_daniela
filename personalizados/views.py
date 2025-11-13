from django.shortcuts import render, redirect
from .models import Personalizado

def personalizados_home(request):
    return render(request, 'personalizados/home.html')

def solicitar_personalizado(request):
    if request.method == 'POST':
        cliente = request.POST.get('cliente')
        email = request.POST.get('email')
        descripcion = request.POST.get('descripcion')
        
        Personalizado.objects.create(
            cliente=cliente,
            email=email,
            descripcion=descripcion
        )
        return redirect('personalizados_gracias')
    
    return render(request, 'personalizados/solicitar.html')

def personalizados_gracias(request):
    return render(request, 'personalizados/gracias.html')