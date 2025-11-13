from django.urls import path
from . import views

urlpatterns = [
    path('', views.personalizados_home, name='personalizados_home'),
    path('solicitar/', views.solicitar_personalizado, name='solicitar_personalizado'),
    path('gracias/', views.personalizados_gracias, name='personalizados_gracias'),
]