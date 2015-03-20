#!/usr/bin/python
# coding=utf-8

from __future__ import unicode_literals
from django.db import models
from dashboard.models import AbstractWidget


class SimpleTextWidget(AbstractWidget):
    content = models.TextField(verbose_name='contenu')

    class Meta():
        verbose_name = 'widget - texte simple'
        verbose_name_plural = 'widgets - texte simple'

    def get_layout(self):
        return 'simple.html'

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

    header = models.CharField(verbose_name='contenu de l\'en-tête', blank=True, max_length=100)
    type = models.CharField(verbose_name='type de texte', choices=TYPE_LIST, default=TYPE_DEFAULT, max_length=100)
    content = models.TextField(verbose_name='contenu du bloc principal')
    footer = models.CharField(verbose_name='contenu du pied de page', blank=True, max_length=100)

    class Meta():
        verbose_name = 'widget - cadre de texte'
        verbose_name_plural = 'widgets - cadre de texte'

    def get_layout(self):
        return 'textwidget/panelwidget/panel.html'

    def get_static_context(self):
        return {'type': self.type,
                'header': self.header,
                'content': self.content,
                'footer': self.footer}


class ClockTextWidget(AbstractWidget):
    format = models.CharField(verbose_name='format de l\'affichage', blank=False, max_length=20,
                              default='dddd DD/MM, HH:mm:ss',
                              help_text='Consultez <a href="http://momentjs.com/docs/#/displaying/">ce lien</a> pour '
                                        'connaître les différents éléments pouvant être utilisés dans le format.')
    delay = models.IntegerField(verbose_name='décalage de l\'heure', default=0,
                                help_text='Le décalage à appliquer sur l\'heure, exprimé en secondes. '
                                          'Ce décalage peut être positif ou négatif.')

    class Meta():
        verbose_name = 'widget - date et heure'
        verbose_name_plural = 'widgets - date et heure'

    def get_layout(self):
        return 'textwidget/clockwidget/clock.html'

    def get_static_context(self):
        return {'format': self.format,
                'delay': self.delay}