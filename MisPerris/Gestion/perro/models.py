from django.db import models
from Gestion.adopcion.models import Persona
# Create your models here.



class Perrito(models.Model):
    nombre = models.CharField(max_length=50)
    sexo = models.CharField(max_length=10)
    edad_aproximada = models.IntegerField()
    fecha_ingreso = models.DateField()
    foto_perro = models.ImageField(upload_to='img', default='DEFAULT_VALUE')
    persona = models.ForeignKey(Persona, null=True, blank=True, on_delete=models.CASCADE)


