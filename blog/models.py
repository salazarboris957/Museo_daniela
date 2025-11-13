from django.db import models
from galeria.models import Obra

class ArticuloBlog(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    imagen_portada = models.ImageField(upload_to='blog/')
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    etiquetas = models.CharField(max_length=200)
    relacionado_obra = models.ForeignKey(Obra, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.titulo