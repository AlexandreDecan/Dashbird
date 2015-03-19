#!/usr/bin/python
# coding=utf-8

from __future__ import unicode_literals
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse_lazy
from django.db import models
from django.db.models import Q


class RegisteredDisplayManager(models.Manager):
    def get_queryset(self):
        return super(RegisteredDisplayManager, self).get_queryset().filter(dashboard__isnull=False)


class Display(models.Model):
    identifier = models.CharField(verbose_name='Identifiant', blank=False, max_length=100, unique=True)
    name = models.CharField(verbose_name='Nom', blank=True, max_length=100)
    description = models.TextField(verbose_name='Description', blank=True)
    dashboard = models.ForeignKey('Dashboard', verbose_name='Dashboard', null=True)
    created_date = models.DateTimeField(verbose_name='Date de création', auto_now_add=True)

    objects = models.Manager()
    registered = RegisteredDisplayManager()

    class Meta():
        verbose_name = 'Affichage'

    def get_absolute_url(self):
        return reverse_lazy('display', kwargs={'display_identifier': self.identifier})

    def __unicode__(self):
        return '{name}<{identifier}>'.format(name=self.name, identifier=self.identifier)


class Dashboard(models.Model):
    HEADER_LAYOUT_DEFAULT = 'navbar.html'
    HEADER_LAYOUT_LIST = [
        (HEADER_LAYOUT_DEFAULT, 'Barre de navigation'),
    ]

    MAIN_LAYOUT_DEFAULT = '3cols.html'
    MAIN_LAYOUT_LIST = [
        (MAIN_LAYOUT_DEFAULT, '3 colonnes'),
    ]

    FOOTER_LAYOUT_DEFAULT = 'nothing.html'
    FOOTER_LAYOUT_LIST = [
        (FOOTER_LAYOUT_DEFAULT, 'Aucun'),
    ]

    STYLE_DEFAULT = 'bootstrap-theme.min.css'
    STYLE_LIST = [
        (STYLE_DEFAULT, 'Par défaut'),
        ('slate.min.css', 'Slate'),
    ]

    name = models.CharField(verbose_name='Nom', blank=False, max_length=100)
    description = models.TextField(verbose_name='Description', blank=True)
    header_layout = models.CharField(verbose_name='Haut de page', max_length=100, choices=HEADER_LAYOUT_LIST, default=HEADER_LAYOUT_DEFAULT)
    main_layout = models.CharField(verbose_name='Corps de page', max_length=100, choices=MAIN_LAYOUT_LIST, default=MAIN_LAYOUT_DEFAULT)
    footer_layout = models.CharField(verbose_name='Pied de page', max_length=100, choices=FOOTER_LAYOUT_LIST, default=FOOTER_LAYOUT_DEFAULT)
    style = models.CharField(verbose_name='Thème', max_length=100, choices=STYLE_LIST, default=STYLE_DEFAULT)
    auto_refresh = models.IntegerField(verbose_name='Rafraichissement', default=0,
                                       help_text='en secondes (<=0 pour désactiver)')

    class Meta():
        verbose_name = 'Dashboard'

    def __unicode__(self):
        return '{name}'.format(name=self.name)

    def get_header_layout(self):
        return 'dashboard/header/' + self.header_layout

    def get_main_layout(self):
        return 'dashboard/main/' + self.main_layout

    def get_footer_layout(self):
        return 'dashboard/footer/' + self.footer_layout

    def get_style(self):
        return 'dashboard/style/' + self.style

    @property
    def cells(self):
        cells = {}
        for cell in Cell.objects.filter(dashboard=self):
            cells[cell.position] = cell
        return cells


class Cell(models.Model):
    dashboard = models.ForeignKey('Dashboard')
    position = models.CharField(verbose_name='Position', blank=False, max_length=100)
    content_type = models.ForeignKey(ContentType,
                                     limit_choices_to=Q(app_label__icontains="widget",
                                                        model__icontains="widget"))
    object_id = models.PositiveIntegerField()
    widget = GenericForeignKey('content_type', 'object_id')

    class Meta():
        verbose_name = 'Association'

    def __unicode__(self):
        return '{dashboard}[{position}]->{widget}'.format(
            dashboard=self.dashboard,
            position=self.position,
            widget=self.widget
        )


class AbstractWidget(models.Model):
    name = models.CharField(verbose_name='Nom', blank=False, max_length=100)
    created = models.DateTimeField(verbose_name='Date de création', auto_now_add=True)
    modified = models.DateTimeField(verbose_name='Date de modification', auto_now=True)

    def __unicode__(self):
        return self.name

    def get_layout(self):
        raise NotImplementedError

    def get_static_context(self):
        raise NotImplementedError

    class Meta:
        abstract = True