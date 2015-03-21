#!/usr/bin/python
# coding=utf-8

from __future__ import unicode_literals
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse_lazy
from django.db import models
from django.db.models import Q
from django.db.models.signals import post_delete
from django.dispatch import receiver

from Dashbird.tools import ChoicesFromDir


class RegisteredDisplayManager(models.Manager):
    def get_queryset(self):
        return super(RegisteredDisplayManager, self).get_queryset().filter(dashboard__isnull=False)


class Display(models.Model):
    identifier = models.CharField(verbose_name='identifiant unique', blank=False, max_length=100,
                                  unique=True, help_text='Ne modifiez cette valeur que si vous savez ce '
                                                         'que vous faites !')
    name = models.CharField(verbose_name='nom', blank=True, max_length=100,
                            help_text='Par exemple : "Hall principal" ou "Couloir extérieur"')
    description = models.TextField(verbose_name='description', blank=True,
                                   help_text='Vous pouvez préciser le public auquel s\'adresse cet affichage.')
    dashboard = models.ForeignKey('Dashboard', null=True, on_delete=models.SET_NULL)
    created_date = models.DateTimeField(verbose_name='date de création', auto_now_add=True)

    objects = models.Manager()
    registered = RegisteredDisplayManager()

    class Meta():
        verbose_name = 'dispositif d\'affichage'
        verbose_name_plural = 'dispositifs d\'affichage'

    def get_absolute_url(self):
        return reverse_lazy('display', kwargs={'display_identifier': self.identifier})

    def __unicode__(self):
        return '{name}<{identifier}>'.format(name=self.name, identifier=self.identifier)


class Dashboard(models.Model):
    HEADER_LAYOUT_LIST = ChoicesFromDir('dashboard/templates/dashboard/header/', '(?P<name>.*)\.html')
    HEADER_LAYOUT_DEFAULT = 'navbar.html'

    MAIN_LAYOUT_LIST = ChoicesFromDir('dashboard/templates/dashboard/main/', '(?P<name>.*)\.html')
    MAIN_LAYOUT_DEFAULT = '1x3.html'

    FOOTER_LAYOUT_LIST = ChoicesFromDir('dashboard/templates/dashboard/footer/', '(?P<name>.*)\.html')
    FOOTER_LAYOUT_DEFAULT = 'nothing.html'

    STYLE_LIST = ChoicesFromDir('dashboard/static/dashboard/style/', '(?P<name>.*)\.min\.css')
    STYLE_DEFAULT = 'default.min.css'

    name = models.CharField(verbose_name='nom du dashboard', blank=False, max_length=100)
    description = models.TextField(verbose_name='description', blank=True,
                                   help_text='Par exemple: les personnes ou les lieux destinés à l\'usage '
                                             'de ce dashboard.')
    header_layout = models.CharField(verbose_name='mise en page du haut de page', max_length=100,
                                     choices=HEADER_LAYOUT_LIST, default=HEADER_LAYOUT_DEFAULT)
    main_layout = models.CharField(verbose_name='mise en page du corps de page', max_length=100,
                                   choices=MAIN_LAYOUT_LIST, default=MAIN_LAYOUT_DEFAULT)
    footer_layout = models.CharField(verbose_name='mise en page du pied de page', max_length=100,
                                     choices=FOOTER_LAYOUT_LIST, default=FOOTER_LAYOUT_DEFAULT)
    style = models.CharField(verbose_name='thème', max_length=100, choices=STYLE_LIST, default=STYLE_DEFAULT,
                             help_text='Jeu de couleurs et disposition à appliquer.')
    auto_refresh = models.IntegerField(verbose_name='rafraichissement', default=60,
                                       help_text='Le dashboard se rafraîchit automatiquement au bout du nombre de '
                                                 'secondes indiquées. Si ce nombre est plus petit ou égal à 0, le '
                                                 'rafraichissement automatique est désactivé.')

    class Meta():
        verbose_name = 'dashboard'

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
    position = models.CharField(verbose_name='position dans le dashboard', blank=False, max_length=100,
                                help_text='header-x, main-x ou footer-x où x est un nombre (de 1 à ...).')
    content_type = models.ForeignKey(ContentType, verbose_name='type de widget',
                                     limit_choices_to=Q(app_label__icontains="widget",
                                                        model__icontains="widget"))
    object_id = models.PositiveIntegerField(verbose_name='numéro du widget')
    widget = GenericForeignKey('content_type', 'object_id')

    class Meta():
        verbose_name = 'position des widgets'
        verbose_name_plural = 'positions des widgets'

    def __unicode__(self):
        return '{dashboard} ({position}) <-> {widget}'.format(
            dashboard=self.dashboard,
            position=self.position,
            widget=self.widget
        )



@receiver(post_delete)
def remove_orphan_cells(sender, instance, **kwargs):
    """
    This function is called every time a deletion is detected through the system.
    It aims to intercept widget deletion, and to remove the (possibly empty) set of cells that rely on
    the widget, to avoid orphan cells.
    :param sender Class concerned by the deletion
    :param instance Instance (deleted from db!) concerned by the deletion
    :param using Database alias being used
    """
    contenttype = ContentType.objects.get_for_model(instance)
    try:
        cell = Cell.objects.get(content_type=contenttype.pk, object_id=instance.pk)
        cell.delete()
    except Cell.DoesNotExist:
        pass



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