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

TEMPLATE_DIR = 'widgets/listwidget/templates/listwidget/'
TEMPLATE_PUB = 'listwidget/'


class TextEntry(models.Model):
    title = models.CharField(verbose_name='titre', blank=True, max_length=100)
    type = models.CharField(verbose_name='type d\'information', choices=BOOTSTRAP_TYPE, default='', max_length=30)
    content = models.TextField(verbose_name='contenu')
    created = models.DateTimeField(verbose_name='date de création', auto_now_add=True)
    modified = models.DateTimeField(verbose_name='date de modification', auto_now=True)
    widget = models.ForeignKey('TextListWidget', related_name='entries')

    class Meta():
        verbose_name = 'élement de liste de textes'
        verbose_name_plural = 'élements de liste de textes'

    def __unicode__(self):
        if self.title:
            return self.title
        else:
            return 'Sans titre'


class TextListWidget(AbstractWidget):
    LAYOUT_LIST = ChoicesFromDir(TEMPLATE_DIR + 'list/', '(?P<name>[^_].*)\.html')
    LAYOUT_DEFAULT = 'default.html'

    INNER_LAYOUT_LIST = ChoicesFromDir(TEMPLATE_DIR + 'entry/', '(?P<name>[^_].*)\.html')
    INNER_LAYOUT_DEFAULT = 'panel.html'

    title = models.CharField(verbose_name='titre', blank=True, max_length=100)
    layout = models.CharField(verbose_name='mise en page de la liste',
                              choices=LAYOUT_LIST, default=LAYOUT_DEFAULT, max_length=100)
    inner_layout = models.CharField(verbose_name='apparence des entrées',
                                    choices=INNER_LAYOUT_LIST, default=INNER_LAYOUT_DEFAULT, max_length=100)

    class Meta():
        verbose_name = 'liste de textes'
        verbose_name_plural = 'liste de textes'

    def get_layout(self):
        return TEMPLATE_PUB + 'list/' + self.layout

    def get_static_context(self):
        return {'title': self.title,
                'entries': self.entries.order_by('created'),
                'inner_layout': TEMPLATE_PUB + 'entry/' + self.inner_layout}

    def __unicode__(self):
        return self.name