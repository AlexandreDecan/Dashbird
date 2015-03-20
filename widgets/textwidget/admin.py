#!/usr/bin/python
# coding=utf-8

from __future__ import unicode_literals
from django.contrib import admin
from models import SimpleTextWidget, PanelTextWidget, ClockTextWidget

@admin.register(SimpleTextWidget)
class SimpleTextWidgetAdmin(admin.ModelAdmin):
    list_display = ('name', 'content',)

@admin.register(PanelTextWidget)
class PanelTextWidgetAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'header', 'content')

@admin.register(ClockTextWidget)
class ClockTextWidgetAdmin(admin.ModelAdmin):
    list_display = ('name', 'format', 'delay')