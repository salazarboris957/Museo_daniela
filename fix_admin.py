import os
import django
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'museo_crochet.settings')
django.setup()

from django.contrib.auth import get_user_model
from django.db import IntegrityError

User = get_user_model()

try:
    # Intentar crear superusuario
    user = User.objects.create_superuser(
        username='admin',
        email='salazarboris957@gmail.com', 
        password='admin123'
    )
    print("✅ Superusuario creado exitosamente!")
    print("Usuario: admin")
    print("Email: salazarboris957@gmail.com")
    print("Password: admin123")
except IntegrityError:
    print("⚠️ El usuario 'admin' ya existe")
    # Verificar el usuario existente
    try:
        user = User.objects.get(username='admin')
        print(f"Usuario encontrado: {user.username}")
        # Cambiar la contraseña por si acaso
        user.set_password('admin123')
        user.save()
        print("🔑 Contraseña resetada a: admin123")
    except User.DoesNotExist:
        print("❌ Error inesperado")
except Exception as e:
    print(f"❌ Error: {e}")
