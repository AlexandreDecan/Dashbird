#!/usr/bin/python
# coding=utf-8

from __future__ import unicode_literals
from django.contrib import admin
from models import MissingTeacherEntry, MissingTeacherWidget


class InlineMissingTeacherEntry(admin.TabularInline):
    model = MissingTeacherEntry

    extra = 0


@admin.register(MissingTeacherWidget)
class MissingTeacherWidgetAdmin(admin.ModelAdmin):
    list_display = ('name', 'modified')
    inlines = [InlineMissingTeacherEntry]


