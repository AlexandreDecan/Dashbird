# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TextEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name='Titre', blank=True)),
                ('content', models.TextField(verbose_name='Contenu')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Date de cr\xe9ation')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Date de modification')),
            ],
            options={
                'verbose_name': 'Texte de liste',
                'verbose_name_plural': 'Textes de liste',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TextListWidget',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='Nom')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Date de cr\xe9ation')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Date de modification')),
                ('title', models.CharField(max_length=100, verbose_name='Titre', blank=True)),
            ],
            options={
                'verbose_name': 'Liste de textes',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='textentry',
            name='widget',
            field=models.ForeignKey(related_name='entries', to='listwidget.TextListWidget'),
            preserve_default=True,
        ),
    ]
