from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('coleccion/<int:coleccion_id>/', views.galeria_coleccion, name='galeria_coleccion'),
    path('obra/<int:obra_id>/', views.obra_detalle, name='obra_detalle'),
]