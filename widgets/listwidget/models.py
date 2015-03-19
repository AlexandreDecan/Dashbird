#!/usr/bin/python
# coding=utf-8

from __future__ import unicode_literals
from django.db import models
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

    title = models.CharField(verbose_name='Titre', blank=True, max_length=100)
    content = models.TextField(verbose_name='Contenu')
    type = models.CharField(verbose_name='Type', choices=TYPE_LIST, default=TYPE_DEFAULT, max_length=30)
    created = models.DateTimeField(verbose_name='Date de création', auto_now_add=True)
    modified = models.DateTimeField(verbose_name='Date de modification', auto_now=True)
    widget = models.ForeignKey('TextListWidget', related_name='entries')

    class Meta():
        verbose_name = 'Texte de liste'
        verbose_name_plural = 'Textes de liste'

    def __unicode__(self):
        if self.title:
            return self.title
        else:
            return 'Sans titre'


class TextListWidget(AbstractWidget):
    LAYOUT_DEFAULT = 'vertical.html'
    LAYOUT_LIST = [
        (LAYOUT_DEFAULT, 'Liste verticale'),
    ]

    INNER_LAYOUT_DEFAULT = 'alert.html'
    INNER_LAYOUT_LIST = [
        (INNER_LAYOUT_DEFAULT, 'Petit bloc coloré'),
        ('panel.html', 'Bloc coloré'),
        ('list.html', 'Liste à puces'),
    ]

    title = models.CharField(verbose_name='Titre', blank=True, max_length=100)
    layout = models.CharField(verbose_name='Apparence de la liste',
                              choices=LAYOUT_LIST, default=LAYOUT_DEFAULT, max_length=100)
    inner_layout = models.CharField(verbose_name='Apparence des entrées',
                                    choices=INNER_LAYOUT_LIST, default=INNER_LAYOUT_DEFAULT, max_length=100)

    class Meta():
        verbose_name = 'Liste de textes'
        verbose_name_plural = 'Listes de texte'

    def get_layout(self):
        return 'listwidget/textlistwidget/' + self.layout

    def get_static_context(self):
        return {'title': self.title,
                'entries': self.entries.order_by('created'),
                'inner_layout': 'listwidget/textlistwidget/entries/'+self.inner_layout}
