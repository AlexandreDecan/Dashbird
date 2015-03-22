# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClockWidget',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text="Le nom est obligatoire et permet d'identifier votre widget facilement.", max_length=100, verbose_name='nom')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='date de cr\xe9ation')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='date de modification')),
                ('format', models.CharField(default='dddd DD/MM, HH:mm:ss', help_text='Consultez <a href="http://momentjs.com/docs/#/displaying/">ce lien</a> pour conna\xeetre les diff\xe9rents \xe9l\xe9ments pouvant \xeatre utilis\xe9s dans le format.', max_length=20, verbose_name="format de l'affichage")),
                ('delay', models.IntegerField(default=0, help_text="Le d\xe9calage \xe0 appliquer sur l'heure, exprim\xe9 en secondes. Ce d\xe9calage peut \xeatre positif ou n\xe9gatif.", verbose_name="d\xe9calage de l'heure")),
            ],
            options={
                'verbose_name': 'widget - date et heure',
                'verbose_name_plural': 'widgets - date et heure',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HTMLWidget',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text="Le nom est obligatoire et permet d'identifier votre widget facilement.", max_length=100, verbose_name='nom')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='date de cr\xe9ation')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='date de modification')),
                ('content', models.TextField(help_text='Vous pouvez utiliser du codeHTML dans ce widget.', verbose_name='contenu')),
            ],
            options={
                'verbose_name': 'widget - contenu HTML',
                'verbose_name_plural': 'widgets - contenu HTML',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TextEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name='titre', blank=True)),
                ('type', models.CharField(default='', max_length=30, verbose_name="type d'information", choices=[('default', 'Par d\xe9faut'), ('primary', 'Primaire'), ('success', 'Succ\xe8s'), ('info', 'Information'), ('warning', 'Avertissement'), ('danger', 'Alerte')])),
                ('content', models.TextField(verbose_name='contenu')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='date de cr\xe9ation')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='date de modification')),
            ],
            options={
                'verbose_name': '\xe9lement de liste de textes',
                'verbose_name_plural': '\xe9lements de liste de textes',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TextListWidget',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text="Le nom est obligatoire et permet d'identifier votre widget facilement.", max_length=100, verbose_name='nom')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='date de cr\xe9ation')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='date de modification')),
                ('title', models.CharField(max_length=100, verbose_name='titre', blank=True)),
                ('layout', models.CharField(default='default.html', max_length=100, verbose_name='mise en page de la liste', choices=[('default.html', 'Default'), ('tab.html', 'Tab'), ('autoscroll.html', 'Autoscroll')])),
                ('inner_layout', models.CharField(default='panel.html', max_length=100, verbose_name='apparence des entr\xe9es', choices=[('alert.html', 'Alert'), ('panel.html', 'Panel'), ('list.html', 'List')])),
            ],
            options={
                'verbose_name': 'widget - liste de textes',
                'verbose_name_plural': 'widgets - liste de textes',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TextWidget',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text="Le nom est obligatoire et permet d'identifier votre widget facilement.", max_length=100, verbose_name='nom')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='date de cr\xe9ation')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='date de modification')),
                ('title', models.CharField(max_length=100, verbose_name='titre', blank=True)),
                ('type', models.CharField(default='', max_length=100, verbose_name='type de texte', choices=[('default', 'Par d\xe9faut'), ('primary', 'Primaire'), ('success', 'Succ\xe8s'), ('info', 'Information'), ('warning', 'Avertissement'), ('danger', 'Alerte')])),
                ('layout', models.CharField(default='panel.html', max_length=100, verbose_name='mise en page', choices=[('alert.html', 'Alert'), ('panel.html', 'Panel'), ('list.html', 'List')])),
                ('content', models.TextField(verbose_name='contenu')),
            ],
            options={
                'verbose_name': 'widget - bloc de texte',
                'verbose_name_plural': 'widgets - bloc de texte',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='textentry',
            name='widget',
            field=models.ForeignKey(related_name='entries', to='basewidget.TextListWidget'),
            preserve_default=True,
        ),
    ]
