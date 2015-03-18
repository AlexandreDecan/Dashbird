# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('textwidget', '0003_auto_20150318_1500'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clocktextwidget',
            options={'verbose_name': 'Date et heure'},
        ),
        migrations.AlterModelOptions(
            name='paneltextwidget',
            options={'verbose_name': 'Cadre de texte'},
        ),
    ]
