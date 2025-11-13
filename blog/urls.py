from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_home, name='blog_home'),
    path('articulo/<int:articulo_id>/', views.articulo_detalle, name='articulo_detalle'),
]