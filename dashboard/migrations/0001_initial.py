# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cell',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('position', models.CharField(max_length=100, verbose_name='Position')),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name': 'Association',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Dashboard',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='Nom')),
                ('description', models.TextField(verbose_name='Description')),
                ('layout', models.CharField(default='dashboard/default.html', max_length=100, verbose_name='Disposition', choices=[('dashboard/default.html', 'Par d\xe9faut')])),
                ('style', models.CharField(default='dashboard/style/default.css', max_length=100, verbose_name='Th\xe8me', choices=[('dashboard/style/default.css', 'Par d\xe9faut')])),
                ('auto_refresh', models.IntegerField(default=-1, help_text='Exprim\xe9 en secondes, -1 pour d\xe9sactiver', verbose_name='D\xe9lai de rafraichissement')),
            ],
            options={
                'verbose_name': 'Dashboard',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Display',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('identifier', models.CharField(unique=True, max_length=100, verbose_name='Identifiant')),
                ('name', models.CharField(max_length=100, verbose_name='Nom')),
                ('description', models.TextField(verbose_name='Description')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Date de cr\xe9ation')),
                ('dashboard', models.ForeignKey(verbose_name='Dashboard', to='dashboard.Dashboard', null=True)),
            ],
            options={
                'verbose_name': 'Affichage',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='cell',
            name='dashboard',
            field=models.ForeignKey(to='dashboard.Dashboard'),
            preserve_default=True,
        ),
    ]
