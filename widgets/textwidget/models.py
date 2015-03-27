#!/usr/bin/python
# coding=utf-8

from __future__ import unicode_literals
from django.db import models
from Dashbird.tools import ChoicesFromDir
from widgets.models import AbstractWidget


BOOTSTRAP_TYPE = [
    ('default', 'Par défaut'),
    ('primary', 'Primaire'),
    ('success', 'Succès'),
    ('info', 'Information'),
    ('warning', 'Avertissement'),
    ('danger', 'Alerte')
]

TEMPLATE_DIR = 'widgets/textwidget/templates/textwidget/'
TEMPLATE_PUB = 'textwidget/'


class HTMLWidget(AbstractWidget):
    content = models.TextField(verbose_name='contenu', blank=False, help_text='Vous pouvez utiliser du code'
                                                                              'HTML dans ce widget.')

    class Meta():
        verbose_name = 'contenu HTML'
        verbose_name_plural = 'contenu HTML'

    def get_layout(self):
        return TEMPLATE_PUB + '/HTMLcontent.html'

    def get_static_context(self):
        return {'content': self.content}


class TextWidget(AbstractWidget):
    LAYOUT_LIST = ChoicesFromDir(TEMPLATE_DIR + 'entry/', '(?P<name>[^_].*)\.html')
    LAYOUT_DEFAULT = 'panel.html'

    title = models.CharField(verbose_name='titre', blank=True, max_length=100)
    type = models.CharField(verbose_name='type de texte', choices=BOOTSTRAP_TYPE, default='', max_length=100)
    layout = models.CharField(verbose_name='mise en page',
                              choices=LAYOUT_LIST, default=LAYOUT_DEFAULT, max_length=100)
    content = models.TextField(verbose_name='contenu')

    class Meta():
        verbose_name = 'bloc de texte'
        verbose_name_plural = 'bloc de texte'

    def get_layout(self):
        return TEMPLATE_PUB + 'text.html'

    def get_static_context(self):
        return {'layout': TEMPLATE_PUB + 'entry/' + self.layout,
                'entry': self}


class ClockWidget(AbstractWidget):
    format = models.CharField(verbose_name='format de l\'affichage', blank=False, max_length=20,
                              default='dddd DD/MM, HH:mm:ss',
                              help_text='Consultez <a href="http://momentjs.com/docs/#/displaying/">ce lien</a> pour '
                                        'connaître les différents éléments pouvant être utilisés dans le format.')
    delay = models.IntegerField(verbose_name='décalage de l\'heure', default=0,
                                help_text='Le décalage à appliquer sur l\'heure, exprimé en secondes. '
                                          'Ce décalage peut être positif ou négatif.')

    class Meta():
        verbose_name = 'date et heure'
        verbose_name_plural = 'date et heure'

    def get_layout(self):
        return TEMPLATE_PUB + 'clock.html'

    def get_static_context(self):
        return {'format': self.format,
                'delay': self.delay}

