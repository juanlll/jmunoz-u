from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from personas.models import persona


def bienvenido(request):
    no_personas_var = persona.objects.count()
    personas = persona.objects.all()
    return render(request, 'bienvenido.html', {'no_personas': no_personas_var, 'personas': personas})
