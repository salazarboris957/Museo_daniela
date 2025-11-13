from django.db import models
from galeria.models import Obra

class Comentario(models.Model):
    obra = models.ForeignKey(Obra, on_delete=models.CASCADE)
    autor = models.CharField(max_length=100)
    email = models.EmailField()
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    aprobado = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Comentario de {self.autor} en {self.obra.nombre}"