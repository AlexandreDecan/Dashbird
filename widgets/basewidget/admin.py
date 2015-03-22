#!/usr/bin/python
# coding=utf-8

from __future__ import unicode_literals
from django.contrib import admin
from models import HTMLWidget, TextWidget, ClockWidget, TextEntry, TextListWidget


@admin.register(HTMLWidget)
class SimpleTextWidgetAdmin(admin.ModelAdmin):
    list_display = ('name', 'content',)


@admin.register(TextWidget)
class PanelTextWidgetAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'type', 'layout')


@admin.register(ClockWidget)
class ClockTextWidgetAdmin(admin.ModelAdmin):
    list_display = ('name', 'format', 'delay')


class InlineTextEntryAdmin(admin.TabularInline):
    model = TextEntry
    readonly_fields = ('created', 'modified',)
    extra = 0


@admin.register(TextListWidget)
class TextListWidgetAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'layout', 'inner_layout',)
    inlines = [InlineTextEntryAdmin]


