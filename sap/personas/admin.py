from django.contrib import admin

# Register your models here.
from personas.models import persona, Domicilio, empresa

admin.site.register(persona)
admin.site.register(Domicilio)
admin.site.register(empresa)