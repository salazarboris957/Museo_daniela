from django.db import models

class Coleccion(models.Model):
    nombre = models.CharField(max_length=100)
    icono = models.CharField(max_length=10)
    descripcion = models.TextField()
    color = models.CharField(max_length=7)
    
    def __str__(self):
        return f"{self.icono} {self.nombre}"

class Obra(models.Model):
    nombre = models.CharField(max_length=100)
    coleccion = models.ForeignKey(Coleccion, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    historia = models.TextField()
    proceso = models.TextField()
    disponible = models.BooleanField(default=True)
    tags = models.CharField(max_length=200)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nombre

class ObraFoto(models.Model):
    obra = models.ForeignKey(Obra, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='obras/')
    descripcion = models.CharField(max_length=200)
    es_principal = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Foto de {self.obra.nombre}"