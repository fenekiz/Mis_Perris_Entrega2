from django.urls import path



from Gestion.adopcion.views import index_adopcion
app_name = 'Gestion'

urlpatterns = [
     path('index', index_adopcion),
]
