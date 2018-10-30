from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from Gestion.perro.forms import MascotaForm
from Gestion.perro.models import Perrito

# Create your views here.

def index(request):
    return render(request, 'index.html')

def galeria(request):
	return render(request, 'galeria.html')

#  def crearMascota(request):
#  	if request.method == 'POST':
#  		form = MascotaForm(request.POST)
#  		if form.is_valid():
#  			form.save()
#  		return redirect('index')
#   	else:
#  		form = MascotaForm()
#   return render(request, 'perro', {'form':form})


# def listarMascota(request):
#  perrito = Perrito.objects.all()
#  context = {'mascota':perrito}
#  return render(request, 'galeria.html',context)
