#!/usr/bin/python
# coding=utf-8

from __future__ import unicode_literals
from django.db import models
from dashboard.models import AbstractWidget


class SimpleTextWidget(AbstractWidget):
    content = models.TextField(verbose_name='Contenu')

    class Meta():
        verbose_name = 'Texte simple'

    def get_layout(self):
        return 'textwidget/simple_text_widget.html'

    def get_static_context(self):
        return {'content': self.content}


class PanelTextWidget(AbstractWidget):
    TYPE_DEFAULT = 'default'
    TYPE_LIST = [
        (TYPE_DEFAULT, 'Par défaut'),
        ('primary', 'Primaire'),
        ('success', 'Succès'),
        ('info', 'Information'),
        ('warning', 'Avertissement'),
        ('danger', 'Alerte')
    ]

    header = models.CharField(verbose_name='En-tête', blank=True, max_length=100)
    type = models.CharField(verbose_name='Type', choices=TYPE_LIST, default=TYPE_DEFAULT, max_length=100)
    content = models.TextField(verbose_name='Contenu')
    footer = models.CharField(verbose_name='Pied de page', blank=True, max_length=100)

    class Meta():
        verbose_name = 'Cadre de texte'
        verbose_name_plural = 'Cadres de texte'

    def get_layout(self):
        return 'textwidget/panel_text_widget.html'

    def get_static_context(self):
        return {'type': self.type,
                'header': self.header,
                'content': self.content,
                'footer': self.footer}


class ClockTextWidget(AbstractWidget):
    format = models.CharField(verbose_name='Format', blank=False, max_length=20, default='dddd DD/MM, HH:mm:ss',
                              help_text='http://momentjs.com/docs/#/displaying/')
    delay = models.IntegerField(verbose_name='Décalage', default=0,
                                help_text='Décalage positif ou négatif, en seconde')

    class Meta():
        verbose_name = 'Date et heure'
        verbose_name_plural = 'Date et heure'

    def get_layout(self):
        return 'textwidget/clock_text_widget.html'

    def get_static_context(self):
        return {'format': self.format,
                'delay': self.delay}