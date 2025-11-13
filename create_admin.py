import os
import django
from django.conf import settings

if not settings.configured:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'museo_crochet.settings')
    django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

# Verificar si ya existe
if User.objects.filter(username='admin').exists():
    print('⚠️ El usuario admin ya existe')
    user = User.objects.get(username='admin')
    user.set_password('admin123')
    user.save()
    print('🔑 Contraseña actualizada a: admin123')
else:
    # Crear nuevo superusuario
    user = User.objects.create_superuser(
        username='admin',
        email='salazarboris957@gmail.com',
        password='admin123'
    )
    print('✅ Superusuario creado exitosamente!')
    print('Usuario: admin')
    print('Email: salazarboris957@gmail.com')
    print('Password: admin123')

print('💾 Guardando cambios...')
