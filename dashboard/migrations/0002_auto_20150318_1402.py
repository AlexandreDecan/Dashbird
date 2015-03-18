# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dashboard',
            name='auto_refresh',
            field=models.IntegerField(default=0, help_text='en secondes (<=0 pour d\xe9sactiver)', verbose_name='Rafraichissement'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='dashboard',
            name='description',
            field=models.TextField(verbose_name='Description', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='dashboard',
            name='layout',
            field=models.CharField(default='default.html', max_length=100, verbose_name='Disposition', choices=[('default.html', 'Par d\xe9faut')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='dashboard',
            name='style',
            field=models.CharField(default='default.css', max_length=100, verbose_name='Th\xe8me', choices=[('default.css', 'Par d\xe9faut')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='display',
            name='description',
            field=models.TextField(verbose_name='Description', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='display',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Nom', blank=True),
            preserve_default=True,
        ),
    ]
