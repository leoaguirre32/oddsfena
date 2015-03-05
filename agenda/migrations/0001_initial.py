# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=200)),
                ('data_inicio', models.DateField()),
                ('data_termino', models.DateField()),
                ('horario', models.CharField(max_length=50, null=True, blank=True)),
                ('local', models.CharField(max_length=300)),
                ('site', models.URLField(max_length=300, null=True, blank=True)),
                ('email', models.EmailField(max_length=100, null=True, blank=True)),
                ('ativo', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TipoEvento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo_evento', models.CharField(max_length=15)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='evento',
            name='tipo_evento',
            field=models.ForeignKey(to='agenda.TipoEvento'),
            preserve_default=True,
        ),
    ]
