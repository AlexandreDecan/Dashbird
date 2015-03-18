#!/usr/bin/python
# coding=utf-8

from __future__ import unicode_literals
from django.contrib import admin
from models import TextEntry, TextListWidget


class InlineTextEntryAdmin(admin.TabularInline):
    model = TextEntry
    readonly_fields = ('created', 'modified', )
    verbose_name = 'Entrée de texte'
    verbose_name_plural = 'Entrées de texte'
    extra = 1

@admin.register(TextListWidget)
class TextListWidgetAdmin(admin.ModelAdmin):
    list_display = ('name', 'title')
    inlines = [InlineTextEntryAdmin]

