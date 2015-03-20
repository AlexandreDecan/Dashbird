#!/usr/bin/python
# coding=utf-8

from __future__ import unicode_literals
from django.db import models
from Dashbird.tools import LazyListDir
from dashboard.models import AbstractWidget


class TextEntry(models.Model):
    TYPE_DEFAULT = 'default'
    TYPE_LIST = [
        (TYPE_DEFAULT, 'Aucun'),
        ('info', 'Information'),
        ('success', 'Succès'),
        ('warning', 'Avertissement'),
        ('danger', 'Alerte'),
    ]

    title = models.CharField(verbose_name='titre', blank=True, max_length=100)
    content = models.TextField(verbose_name='contenu')
    type = models.CharField(verbose_name='type d\'information', choices=TYPE_LIST, default=TYPE_DEFAULT, max_length=30)
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
    LAYOUT_LIST = LazyListDir('widgets/listwidget/templates/listwidget/textlistwidget/', '(?P<name>.*)\.html')
    LAYOUT_DEFAULT = 'vertical.html'

    INNER_LAYOUT_LIST = LazyListDir('widgets/listwidget/templates/listwidget/textlistwidget/entries/', '(?P<name>.*)\.html')
    INNER_LAYOUT_DEFAULT = 'alert.html'

    title = models.CharField(verbose_name='titre', blank=True, max_length=100)
    layout = models.CharField(verbose_name='mise en page de la liste',
                              choices=LAYOUT_LIST, default=LAYOUT_DEFAULT, max_length=100)
    inner_layout = models.CharField(verbose_name='apparence des entrées',
                                    choices=INNER_LAYOUT_LIST, default=INNER_LAYOUT_DEFAULT, max_length=100)

    class Meta():
        verbose_name = 'widget - liste de textes'
        verbose_name_plural = 'widgets - liste de textes'

    def get_layout(self):
        return 'listwidget/textlistwidget/' + self.layout

    def get_static_context(self):
        return {'title': self.title,
                'entries': self.entries.order_by('created'),
                'inner_layout': 'listwidget/textlistwidget/entries/'+self.inner_layout}

    def __unicode__(self):
        return self.name