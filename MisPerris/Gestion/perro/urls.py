from django.urls import path

from Gestion.perro.views import index
from Gestion.perro.views import galeria

app_name = 'Gestion'


urlpatterns = [
     path('', index, name='index'),
    #  path('crea_mascota', crearMascota, name="crear_mascota")
    # path('listar_mascota/',listarMascota, name="listar_mascota")
    path('galeria/', galeria ,name='galeria'),
    
]
