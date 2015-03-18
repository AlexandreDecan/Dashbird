# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listwidget', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='textlistwidget',
            options={'verbose_name': 'Liste de textes', 'verbose_name_plural': 'Listes de texte'},
        ),
        migrations.AddField(
            model_name='textlistwidget',
            name='inner_layout',
            field=models.CharField(default='_text_entry.html', max_length=100, verbose_name='Disposition des entr\xe9es', choices=[('_text_entry.html', 'Par d\xe9faut')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='textlistwidget',
            name='layout',
            field=models.CharField(default='text_list_widget.html', max_length=100, verbose_name='Disposition', choices=[('text_list_widget.html', 'Par d\xe9faut')]),
            preserve_default=True,
        ),
    ]
