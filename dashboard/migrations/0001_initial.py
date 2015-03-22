# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cell',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('position', models.CharField(help_text='header-x, main-x ou footer-x o\xf9 x est un nombre (de 1 \xe0 ...).', max_length=100, verbose_name='position dans le dashboard')),
                ('object_id', models.PositiveIntegerField(verbose_name='num\xe9ro du widget')),
                ('content_type', models.ForeignKey(verbose_name='type de widget', to='contenttypes.ContentType')),
            ],
            options={
                'verbose_name': 'position des widgets',
                'verbose_name_plural': 'positions des widgets',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Dashboard',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='nom du dashboard')),
                ('description', models.TextField(help_text="Par exemple: les personnes ou les lieux destin\xe9s \xe0 l'usage de ce dashboard.", verbose_name='description', blank=True)),
                ('header_layout', models.CharField(default='navbar.html', max_length=100, verbose_name='mise en page du haut de page', choices=[('navbar.html', 'Navbar')])),
                ('main_layout', models.CharField(default='1x3.html', max_length=100, verbose_name='mise en page du corps de page', choices=[('1x3.html', '1X3')])),
                ('footer_layout', models.CharField(default='nothing.html', max_length=100, verbose_name='mise en page du pied de page', choices=[('nothing.html', 'Nothing')])),
                ('style', models.CharField(default='default.min.css', help_text='Jeu de couleurs et disposition \xe0 appliquer.', max_length=100, verbose_name='th\xe8me', choices=[('bootstrap-theme.min.css', 'Bootstrap Theme'), ('superhero.min.css', 'Superhero'), ('lumen.min.css', 'Lumen'), ('default.min.css', 'Default'), ('cerulean.min.css', 'Cerulean'), ('slate.min.css', 'Slate')])),
                ('auto_refresh', models.IntegerField(default=120, help_text='Le dashboard se rafra\xeechit automatiquement au bout du nombre de secondes indiqu\xe9es. Si ce nombre est plus petit ou \xe9gal \xe0 0, le rafraichissement automatique est d\xe9sactiv\xe9.', verbose_name='rafraichissement')),
            ],
            options={
                'verbose_name': 'dashboard',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Display',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('identifier', models.CharField(help_text='Ne modifiez cette valeur que si vous savez ce que vous faites !', unique=True, max_length=100, verbose_name='identifiant unique')),
                ('name', models.CharField(help_text='Par exemple : "Hall principal" ou "Couloir ext\xe9rieur"', max_length=100, verbose_name='nom', blank=True)),
                ('description', models.TextField(help_text="Vous pouvez pr\xe9ciser le public auquel s'adresse cet affichage.", verbose_name='description', blank=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='date de cr\xe9ation')),
                ('dashboard', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, to='dashboard.Dashboard', null=True)),
            ],
            options={
                'verbose_name': "dispositif d'affichage",
                'verbose_name_plural': "dispositifs d'affichage",
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
