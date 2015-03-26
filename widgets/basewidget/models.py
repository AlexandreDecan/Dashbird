#!/usr/bin/python
# coding=utf-8

from __future__ import unicode_literals
from django.db import models
from Dashbird.tools import ChoicesFromDir


BOOTSTRAP_TYPE = [
    ('default', 'Par défaut'),
    ('primary', 'Primaire'),
    ('success', 'Succès'),
    ('info', 'Information'),
    ('warning', 'Avertissement'),
    ('danger', 'Alerte')
]

TEMPLATE_DIR = 'widgets/basewidget/templates/basewidget/'
TEMPLATE_PUB = 'basewidget/'


class AbstractWidget(models.Model):
    name = models.CharField(verbose_name='nom', blank=False, max_length=100,
                            help_text='Le nom est obligatoire et permet d\'identifier votre widget facilement.')
    created = models.DateTimeField(verbose_name='date de création', auto_now_add=True)
    modified = models.DateTimeField(verbose_name='date de modification', auto_now=True)

    @property
    def classname(self):
        return self.__class__.__name__

    @property
    def wuid(self):
        return '{classname}-{id}'.format(classname=self.classname, id=self.pk)

    def __unicode__(self):
        return self.name

    def get_layout(self):
        raise NotImplementedError

    def get_static_context(self):
        raise NotImplementedError

    class Meta:
        abstract = True
        ordering = ('name',)


class HTMLWidget(AbstractWidget):
    content = models.TextField(verbose_name='contenu', blank=False, help_text='Vous pouvez utiliser du code'
                                                                              'HTML dans ce widget.')

    class Meta():
        verbose_name = 'contenu HTML'
        verbose_name_plural = 'contenu HTML'

    def get_layout(self):
        return 'basewidget/HTMLcontent.html'

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