# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('textwidget', '0004_auto_20150318_1507'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clocktextwidget',
            options={'verbose_name': 'Date et heure', 'verbose_name_plural': 'Date et heure'},
        ),
        migrations.AlterModelOptions(
            name='paneltextwidget',
            options={'verbose_name': 'Cadre de texte', 'verbose_name_plural': 'Cadres de texte'},
        ),
        migrations.RenameField(
            model_name='paneltextwidget',
            old_name='title',
            new_name='header',
        ),
        migrations.AlterField(
            model_name='clocktextwidget',
            name='format',
            field=models.CharField(default='dddd DD/MM, HH:mm:ss', help_text='http://momentjs.com/docs/#/displaying/', max_length=20, verbose_name='Format'),
            preserve_default=True,
        ),
    ]
