#!/usr/bin/python
# coding=utf-8

from __future__ import unicode_literals
from django.contrib import admin
from models import HTMLWidget, TextWidget, ClockWidget


@admin.register(HTMLWidget)
class SimpleTextWidgetAdmin(admin.ModelAdmin):
    list_display = ('name', 'content',)
    readonly_fields = ('modified',)


@admin.register(TextWidget)
class PanelTextWidgetAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'type', 'layout')
    readonly_fields = ('modified',)


@admin.register(ClockWidget)
class ClockTextWidgetAdmin(admin.ModelAdmin):
    list_display = ('name', 'format', 'delay')

