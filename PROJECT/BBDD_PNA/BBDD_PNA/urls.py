"""BBDD_PNA URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from gestion_BBDD import views                         # importamos "views" desde gestion_BBDD
from django.urls import reverse

# agregamos a la lista de paths "Causas" y "Numerador" 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('causas', views.causas, name="Causas"),
    path('numerador', views.numerador, name="Numerador"),
]



# modificación de la ventana de login
admin.site.site_header = "DIRECCIÓN DE INTELIGENCIA E INVESTIGACIÓN CRIMINAL"              # Permite setear el título de la ventana de logeo
admin.site.site_title = "DIRECCIÓN DE INTELIGENCIA E INVESTIGACIÓN CRIMINAL"               # Permite setear el nombre al costado izquierdo superior de sitio
admin.site.index_title = ""
