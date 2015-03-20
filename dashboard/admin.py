#!/usr/bin/python
# coding=utf-8

from __future__ import unicode_literals
from django.contrib import admin

from models import Display, Dashboard, Cell


@admin.register(Display)
class DisplayAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('identifier', 'name', 'dashboard', 'description')
    search_fields = ('identifier', 'name', 'description')
    list_filter = ('dashboard__name',)
    ordering = ('name',)


@admin.register(Dashboard)
class DashboardAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'header_layout', 'main_layout', 'footer_layout', 'style')
    search_fields = ('name', 'description')
    ordering = ('name',)


@admin.register(Cell)
class CellAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'dashboard', 'position', 'content_type', 'widget')
    list_filter = ('dashboard', 'position', )
    ordering = ('dashboard__name',)

    related_lookup_fields = {
        'generic': [['content_type', 'object_id']],
    }

