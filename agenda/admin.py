from django.contrib import admin
from .models import Evento, TipoEvento

# Register your models here.

admin.site.register(Evento)
admin.site.register(TipoEvento)