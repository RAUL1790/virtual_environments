# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='nombre',
            field=models.CharField(help_text=b'Ingrese nombre del proyecto', max_length=200, verbose_name=b'Nombre'),
            preserve_default=True,
        ),
    ]
