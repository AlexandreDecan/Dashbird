#!/usr/bin/python
# coding=utf-8

from __future__ import unicode_literals
from django.contrib import admin

from models import Display, Dashboard, Cell


@admin.register(Display)
class DisplayAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    list_display = ('identifier', 'name', 'dashboard')
    search_fields = ('identifier', 'name', 'description')
    list_filter = ('dashboard__name',)
    ordering = ('name',)


@admin.register(Dashboard)
class DashboardAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')
    ordering = ('name',)


@admin.register(Cell)
class CellAdmin(admin.ModelAdmin):
    list_display = ('widget', 'dashboard', 'position', )
    list_filter = ('dashboard__name',)
    ordering = ('dashboard__name',)



