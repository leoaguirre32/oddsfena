from django.shortcuts import render
from .models import Evento
from django.forms.models import model_to_dict
# Create your views here.

def eventos(request):

    eventos = Evento.objects.filter(ativo=True)
    temp = []
    periodo = []
    for evento in eventos:
        if not {'mes': evento.data_inicio.month, 'ano': evento.data_inicio.year} in periodo:
            temp.append(model_to_dict(evento, fields=['data_inicio']))
            periodo.append({'mes': evento.data_inicio.month, 'ano': evento.data_inicio.year})
    print periodo
    meses = sorted(temp)
    return render(request, 'agenda_eventos.html', {'eventos': eventos, 'meses': meses})