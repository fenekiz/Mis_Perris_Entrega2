from django.conf.urls import url
from Gestion.usuario.views import RegistroUsuario
from django.urls import path
app_name = 'Gestion'

urlpatterns =[
    path('registrar/',RegistroUsuario.as_view(), name='registrar')
    
]