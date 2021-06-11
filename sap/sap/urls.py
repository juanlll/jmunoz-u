"""sap URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from webapp.views import bienvenido
from personas.views import detallepersona, nuevapersona, editarpersona, eliminarpersona, verdireccion, nuevodomicilio, \
    nuevaempresa, detalleempresa, editardomicilio, editarempresa

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', bienvenido, name='index'),
    path('detalle_persona/<int:id>', detallepersona),
    path('nueva_persona', nuevapersona),
    path('editar_persona/<int:id>', editarpersona),
    path('eliminar_persona/<int:id>', eliminarpersona),
    path('ver_direcciones', verdireccion, name='ver_direcciones'),
    path('nuevo_domicilio', nuevodomicilio),
    path('editar_domicilio/<int:id>', editardomicilio),
    path('ver_empresas', detalleempresa),
    path('nueva_empresa', nuevaempresa),
    path('editar_empresa/<int:id>', editarempresa),

]
