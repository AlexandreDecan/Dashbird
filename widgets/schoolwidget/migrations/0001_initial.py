# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MissingTeacherEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hour', models.PositiveIntegerField(verbose_name='Heure de cours')),
                ('content', models.TextField(verbose_name='contenu', blank=True)),
                ('visible', models.BooleanField(default=True, verbose_name='visible ?')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='date de cr\xe9ation')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='date de modification')),
            ],
            options={
                'verbose_name': 'heure de cours',
                'verbose_name_plural': 'heures de cours',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MissingTeacherWidget',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text="Le nom est obligatoire et permet d'identifier votre widget facilement.", max_length=100, verbose_name='nom')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='date de cr\xe9ation')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='date de modification')),
                ('missing', models.TextField(help_text='Un enseignant par ligne.', verbose_name='Enseignants absents', blank=True)),
                ('hide_empty', models.BooleanField(default=True, help_text="Masque les heures de cours pour lesquelles aucuneinformation n'a \xe9t\xe9 entr\xe9e.", verbose_name='Cacher les \xe9l\xe9ments vides')),
            ],
            options={
                'verbose_name': 'enseignant absent',
                'verbose_name_plural': 'enseignants absents',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='missingteacherentry',
            name='widget',
            field=models.ForeignKey(related_name='hours', to='schoolwidget.MissingTeacherWidget'),
            preserve_default=True,
        ),
    ]
