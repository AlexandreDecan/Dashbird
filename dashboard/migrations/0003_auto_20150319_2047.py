# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20150318_1402'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dashboard',
            name='layout',
        ),
        migrations.AddField(
            model_name='dashboard',
            name='footer_layout',
            field=models.CharField(default='nothing.html', max_length=100, verbose_name='Pied de page', choices=[('nothing.html', 'Aucun')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dashboard',
            name='header_layout',
            field=models.CharField(default='navbar.html', max_length=100, verbose_name='Haut de page', choices=[('navbar.html', 'Barre de navigation')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dashboard',
            name='main_layout',
            field=models.CharField(default='3cols.html', max_length=100, verbose_name='Corps de page', choices=[('3cols.html', '3 colonnes')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='dashboard',
            name='style',
            field=models.CharField(default='bootstrap-theme.min.css', max_length=100, verbose_name='Th\xe8me', choices=[('bootstrap-theme.min.css', 'Par d\xe9faut'), ('slate.min.css', 'Slate')]),
            preserve_default=True,
        ),
    ]
