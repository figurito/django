from datetime import datetime
from django.db import models


# Create your models here.
class persona(models.Model):
    nombre= models.CharField(max_length=15)
    telefono=models.CharField(max_length=12)
    fecha_n=models.DateField()
    correo=models.EmailField(max_length=150)
    genero=models.CharField(max_length=10)
    created_at = models.DateTimeField(default=datetime.now, null=True, blank=True, editable=False)

    def __str__(self):
        return str(self.nombre) + " || " + str(self.created_at)