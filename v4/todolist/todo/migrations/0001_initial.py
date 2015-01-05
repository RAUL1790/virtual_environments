# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(help_text=b'Ingrese nombre del proyecto', max_length=200, null=True, verbose_name=b'Nombre', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TodoArticulo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tarea', models.TextField(help_text=b'Descripcion de la tarea', verbose_name=b'Tareas')),
                ('fecha', models.DateField()),
                ('fktodo', models.ForeignKey(to='todo.Todo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
