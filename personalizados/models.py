from django.db import models

class Personalizado(models.Model):
    ESTADOS = [
        ('solicitado', '📥 Solicitado'),
        ('cotizado', '💰 Cotizado'),
        ('en_proceso', '🎨 En Proceso'),
        ('completado', '✅ Completado'),
        ('entregado', '🎉 Entregado')
    ]
    
    cliente = models.CharField(max_length=100)
    email = models.EmailField()
    descripcion = models.TextField()
    referencia = models.ImageField(upload_to='referencias/', blank=True)
    presupuesto = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='solicitado')
    fecha_solicitud = models.DateTimeField(auto_now_add=True)
    historia_publica = models.TextField(blank=True)
    
    def __str__(self):
        return f"Pedido de {self.cliente}"

class ProcesoPersonalizado(models.Model):
    personalizado = models.ForeignKey(Personalizado, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='proceso_personalizados/')
    descripcion = models.CharField(max_length=200)
    fecha = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Proceso para {self.personalizado.cliente}"