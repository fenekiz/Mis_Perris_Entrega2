from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistroForm(UserCreationForm):

    class meta:
        model = User
        fields = [
            'username'
            'password'
            'edad',
            'email',
            'rut',
            'telefono'

        ]
        labels = {
            'username' : 'Nombre de usuario',
            'password' : 'Contraseña',
            'edad' : 'Edad',
            'email' : 'Correo' ,
            'rut' : 'RUT',
            'telefono' : 'Telefono'
        }