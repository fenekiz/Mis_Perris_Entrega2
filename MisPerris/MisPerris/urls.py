"""MisPerris URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin, sites
# from django.contrib.auth.views import *
from django.urls import path
# from django.conf.urls import *
from django.conf.urls.static import static
from django.conf import settings
# from django.contrib.auth import *
from django.conf.urls import url, include
from django.contrib import admin

from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.contrib.auth import views as auth_views
APP_NAME = 'Gestion'


urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('perro/', include('Gestion.perro.urls', namespace="perro")),
    path('adopcion/', include('Gestion.adopcion.urls', namespace="adopcion")),
    path('usuario/', include('Gestion.usuario.urls',namespace='usuario')),
    path('galeria',include('Gestion.perro.urls', namespace="galeria")),
    path('', LoginView.as_view(template_name='login.html'), name="login"),
    path('reset/password_reset', PasswordResetView, {'template_name':'registration/password_reset_form.html', 'email_template_name':'registration/password_reset_email.html'},name ="password_reset"),
    path('reset/password_reset_done', PasswordResetDoneView, {'template_name':'registration/password_reset_done.html'}, name="password_reset_done"),
    path('reset/<}<uidb64/<token>', PasswordResetConfirmView, {'template_name':'registration/password_reset_confirm.html'}, name="password_reset_confirm"),
    path('reset/done',PasswordResetCompleteView, {'template_name':'registration/password_reset_complete.html'}, name="passowrd_reset_complete"),
]+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
