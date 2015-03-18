# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listwidget', '0002_auto_20150318_1602'),
    ]

    operations = [
        migrations.AddField(
            model_name='textentry',
            name='type',
            field=models.CharField(default='info', max_length=30, verbose_name='Type', choices=[('info', 'Information'), ('success', 'Succ\xe8s'), ('warning', 'Avertissement'), ('danger', 'Alerte')]),
            preserve_default=True,
        ),
    ]
