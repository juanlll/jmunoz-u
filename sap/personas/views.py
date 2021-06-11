from django.forms import modelform_factory
from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.

from personas.models import persona, Domicilio, empresa

from personas.forms import PersonaForms, domicilioForms, empresaForms


#Vistas de la página
#---------DIRECCION-----------
def verdireccion(request):
    #cosa = persona.objects.get(pk=id)
    cosa = Domicilio.objects.all
    return render(request, 'domicilio/detalledirecciones.html', {'Direccion': cosa})

def nuevodomicilio(request):
    if request.method == 'POST':
        formaDomicilio = domicilioForms(request.POST)
        if formaDomicilio.is_valid():
            formaDomicilio.save()
            return redirect('ver_direcciones')

    else:
        formaDomicilio = domicilioForms()
    return render(request, 'domicilio/nuevodomicilio.html', {'formaDomicilio': formaDomicilio})

def editardomicilio(request, id):
    cosa1 = get_object_or_404(Domicilio, pk=id)
    if request.method == 'POST':
        formaDomicilio = domicilioForms(request.POST, instance=cosa1)
        if formaDomicilio.is_valid():
            formaDomicilio.save()
            return redirect('index')

    else:
        formaDomicilio = domicilioForms(instance=cosa1)
    return render(request, 'domicilio/editardomicilio.html', {'formaDomicilio': formaDomicilio})


#---------PERSONA-----------

def detallepersona(request, id):
    #cosa = persona.objects.get(pk=id)
    cosa = get_object_or_404(persona, pk=id)
    return render(request, 'personas/detallepersonas.html', {'persona': cosa})

#PersonaForm = modelform_factory(persona, exclude=[])

def nuevapersona(request):
    if request.method == 'POST':
        formaPersona = PersonaForms(request.POST)
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect('index')

    else:
        formaPersona = PersonaForms()
    return render(request, 'personas/nuevapersona.html', {'formaPersona': formaPersona})


def editarpersona(request, id):
    cosa = get_object_or_404(persona, pk=id)
    if request.method == 'POST':
        formaPersona = PersonaForms(request.POST, instance=cosa)
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect('index')

    else:
        formaPersona = PersonaForms(instance=cosa)
    return render(request, 'personas/nuevapersona.html', {'formaPersona': formaPersona})

def eliminarpersona(request, id):
    cosa = get_object_or_404(persona, pk=id)

    if cosa:
        cosa.delete()
    return redirect('index')

#---------EMPRESA-----------

def detalleempresa(request):
    #cosa = persona.objects.get(pk=id)
    cosa = empresa.objects.all
    return render(request, 'empresa/detalleempresa.html', {'Empresa': cosa})

#PersonaForm = modelform_factory(persona, exclude=[])

def nuevaempresa(request):
    if request.method == 'POST':
        formaEmpresa = empresaForms(request.POST)
        if formaEmpresa.is_valid():
            formaEmpresa.save()
            return redirect('index')

    else:
        formaEmpresa = empresaForms()
    return render(request, 'empresa/nuevaempresa.html', {'formaEmpresa': formaEmpresa})

def editarempresa(request, id):
    cosa = get_object_or_404(empresa, pk=id)
    if request.method == 'POST':
        formaEmpresa = empresaForms(request.POST, instance=cosa)
        if formaEmpresa.is_valid():
            formaEmpresa.save()
            return redirect('index')

    else:
        formaEmpresa = empresaForms(instance=cosa)
    return render(request, 'empresa/editarempresa.html', {'formaEmpresa': formaEmpresa})
