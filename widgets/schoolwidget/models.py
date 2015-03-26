#!/usr/bin/python
# coding=utf-8

from __future__ import unicode_literals
from django.db import models
from widgets.basewidget.models import AbstractWidget


TEMPLATE_DIR = 'widgets/school/templates/school/'
TEMPLATE_PUB = 'school/'


class MissingTeacherEntry(models.Model):
    hour = models.PositiveIntegerField(verbose_name='Heure de cours')
    content = models.TextField(verbose_name='contenu', blank=True)
    visible = models.BooleanField(verbose_name='visible ?', default=True)
    created = models.DateTimeField(verbose_name='date de création', auto_now_add=True)
    modified = models.DateTimeField(verbose_name='date de modification', auto_now=True)
    widget = models.ForeignKey('MissingTeacherWidget', related_name='hours')

    @property
    def items(self):
        items = []
        for item in self.content.split('\n'):
            try:
                students, change = item.split(' - ', 1)
            except ValueError:
                students, change = item, ''
            items.append((students.strip(),change.strip()))
        return items

    class Meta():
        verbose_name = 'heure de cours'
        verbose_name_plural = 'heures de cours'

    def __unicode__(self):
        return '{hour}h - {content}'.format(hour=self.hour, content=self.content)


class MissingTeacherWidget(AbstractWidget):
    missing = models.TextField(verbose_name='Enseignants absents',blank=True,
                               help_text='Un enseignant par ligne.')
    hide_empty = models.BooleanField(verbose_name='Cacher les éléments vides', default=True,
                                     help_text='Masque les heures de cours pour lesquelles aucune'
                                               'information n\'a été entrée.')

    class Meta():
        verbose_name = 'enseignant absent'
        verbose_name_plural = 'enseignants absents'

    def get_static_context(self):
        hours = self.hours.filter(visible=True).order_by('hour')
        if self.hide_empty:
            hours = hours.exclude(content='')
        return {'modified': self.modified,
                'missing': [p.strip() for p in self.missing.split('\n')],
                'hours': hours}

    def get_layout(self):
        return TEMPLATE_PUB + 'missing/default.html'

