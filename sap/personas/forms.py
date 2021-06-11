from django.forms import ModelForm, EmailInput, TextInput

from personas.models import persona, empresa, Domicilio


class PersonaForms (ModelForm):
    class Meta:
        model = persona
        fields = '__all__'
        widgets = {
            'email': EmailInput(attrs={'type': 'email'})
        }

class empresaForms (ModelForm):
    class Meta:
        model = empresa
        fields = '__all__'
        widgets = {
            'salario': TextInput(attrs={'type': 'number'})
        }

class domicilioForms (ModelForm):
    class Meta:
        model = Domicilio
        fields = '__all__'
        widgets = {
            'no_calle': TextInput(attrs={'type': 'number'})
        }