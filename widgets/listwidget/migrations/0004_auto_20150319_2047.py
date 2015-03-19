# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listwidget', '0003_textentry_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textentry',
            name='type',
            field=models.CharField(default='default', max_length=30, verbose_name='Type', choices=[('default', 'Aucun'), ('info', 'Information'), ('success', 'Succ\xe8s'), ('warning', 'Avertissement'), ('danger', 'Alerte')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='textlistwidget',
            name='inner_layout',
            field=models.CharField(default='alert.html', max_length=100, verbose_name='Apparence des entr\xe9es', choices=[('alert.html', 'Petit bloc color\xe9'), ('panel.html', 'Bloc color\xe9'), ('list.html', 'Liste \xe0 puces')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='textlistwidget',
            name='layout',
            field=models.CharField(default='vertical.html', max_length=100, verbose_name='Apparence de la liste', choices=[('vertical.html', 'Liste verticale')]),
            preserve_default=True,
        ),
    ]
