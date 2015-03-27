#!/usr/bin/python
# coding=utf-8

from __future__ import unicode_literals
from django.db import models


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