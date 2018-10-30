from django import forms
from Gestion.perro.models import Perrito

class MascotaForm(forms.ModelForm):
    model = Perrito
    fields = [
        'nombre',
        'sexo',
        'edad',
        'fecha_ingreso',
        'foto',
        'persona'
    ]
    labels = {
			'nombre': 'Nombre',
			'sexo': 'Sexo',
			'edad_aproximada': 'Edad aproximada',
			'fecha_rescate':'Fecha de rescate',
			'persona': 'Adoptante',
			
		}
    widgets = {
			'nombre': forms.TextInput(attrs={'class':'form-control'}),
			'sexo': forms.TextInput(attrs={'class':'form-control'}),
			'edad_aproximada': forms.TextInput(attrs={'class':'form-control'}),
			'fecha_rescate': forms.TextInput(attrs={'class':'form-control'}),
			'persona': forms.Select(attrs={'class':'form-control'}),
    }