#!/usr/bin/python
# coding=utf-8

from __future__ import unicode_literals
from django.http import Http404
from django.shortcuts import render
from django.views.generic import View

from models import Display


class DisplayView(View):
    def get(self, request, display_identifier=None):
        """
        Check if given display exists. If True, display the associated dashboard.
        Otherwise, register the display and return a 404.

        :param request: Current request
        :param display_identifier: Display identifier
        :return: An HttpResponse
        """

        # Check if display is registered
        try:
            display = Display.objects.get(identifier=display_identifier)
        except Display.DoesNotExist:
            # Registered display
            display = Display(identifier=display_identifier)
            display.save()
            raise Http404()

        # Create context with dashboard and cells
        context = {
            'display': display,
            'dashboard': display.dashboard,
            'cells': display.dashboard.cells
        }

        return render(request, display.dashboard.get_layout(), context)
