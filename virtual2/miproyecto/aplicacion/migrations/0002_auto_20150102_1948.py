# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='apellido',
            field=models.CharField(help_text=b'Ingrese apellido', max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='alumno',
            name='nombre',
            field=models.CharField(help_text=b'Ingrese nombre', max_length=50),
            preserve_default=True,
        ),
    ]
