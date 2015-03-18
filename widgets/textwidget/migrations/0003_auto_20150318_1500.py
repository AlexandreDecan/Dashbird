# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('textwidget', '0002_auto_20150318_1402'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClockTextWidget',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='Nom')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Date de cr\xe9ation')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Date de modification')),
                ('format', models.CharField(help_text='http://momentjs.com/docs/#/displaying/', max_length=20, verbose_name='Format')),
                ('delay', models.IntegerField(default=0, help_text='D\xe9calage positif ou n\xe9gatif, en seconde', verbose_name='D\xe9calage')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PanelTextWidget',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='Nom')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Date de cr\xe9ation')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Date de modification')),
                ('title', models.CharField(max_length=100, verbose_name='En-t\xeate', blank=True)),
                ('type', models.CharField(default='default', max_length=100, verbose_name='Type', choices=[('default', 'Par d\xe9faut'), ('primary', 'Primaire'), ('success', 'Succ\xe8s'), ('info', 'Information'), ('warning', 'Avertissement'), ('danger', 'Alerte')])),
                ('content', models.TextField(verbose_name='Contenu')),
                ('footer', models.CharField(max_length=100, verbose_name='Pied de page', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='simpletextwidget',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 18, 15, 0, 11, 401364), verbose_name='Date de cr\xe9ation', auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='simpletextwidget',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2015, 3, 18, 15, 0, 20, 345240), verbose_name='Date de modification', auto_now=True),
            preserve_default=False,
        ),
    ]
