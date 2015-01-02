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
                ('nombre', models.CharField(help_text=b'Ingrese el nombre del proyecto', max_length=200, verbose_name=b'Nombre')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TodoArticulo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tarea', models.TextField(help_text=b'Descripcion dela tarea', verbose_name=b'Tareas')),
                ('fecha', models.DateField()),
                ('fKtodo', models.ForeignKey(to='todo.Todo')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
