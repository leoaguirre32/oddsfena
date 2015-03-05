from django.db import models

# Create your models here.

class TipoEvento(models.Model):

    tipo_evento = models.CharField(max_length=15, blank=False, null=False)

    def __unicode__(self):
        return self.tipo_evento

class Evento(models.Model):

    tipo_evento = models.ForeignKey(TipoEvento)
    titulo = models.CharField(max_length=200, blank=False, null=False)
    data_inicio = models.DateField(blank=False, null=False)
    data_termino = models.DateField(blank=False, null=False)
    horario = models.CharField(max_length=50, blank=True, null=True)
    local = models.CharField(max_length=300, blank=False, null=False)
    site = models.URLField(max_length=300, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    ativo = models.BooleanField(blank=False, null=False, default=True)

    def __unicode__(self):
        return self.titulo