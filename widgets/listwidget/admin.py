#!/usr/bin/python
# coding=utf-8

from __future__ import unicode_literals
from django.contrib import admin
from models import TextEntry, TextListWidget


class InlineTextEntryAdmin(admin.TabularInline):
    model = TextEntry
    readonly_fields = ('modified',)
    extra = 0


@admin.register(TextListWidget)
class TextListWidgetAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'layout', 'inner_layout',)
    readonly_fields = ('modified',)
    inlines = [InlineTextEntryAdmin]


