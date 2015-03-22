#!/usr/bin/python
# coding=utf-8

from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.urlresolvers import reverse_lazy
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import View

from models import Display, Dashboard


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
            display = Display.registered.get(identifier=display_identifier)
        except Display.DoesNotExist:
            try:
                Display.objects.get(identifier=display_identifier)
                # Is not registered but exists, do nothing
                raise Http404()
            except Display.DoesNotExist:
                # really does not exist
                display = Display(identifier=display_identifier)
                display.save()
                raise Http404()

        # At this point, `display` contains a valid Display instance

        context = {
            'display': display,
            'dashboard': display.dashboard,
            'cells': display.dashboard.cells
        }

        return render(request, 'dashboard/dashboard.html', context)


class DashboardView(View):

    @method_decorator(user_passes_test(lambda u: u.is_staff, login_url=reverse_lazy('admin:index')))
    def dispatch(self, *args, **kwargs):
        return super(DashboardView, self).dispatch(*args, **kwargs)

    def get(self, request, dashboard_id=None):
        try:
            dashboard = Dashboard.objects.get(id=dashboard_id)
        except Dashboard.DoesNotExist:
            raise Http404()

        context = {
            'display': None,
            'dashboard': dashboard,
            'cells': dashboard.cells
        }

        return render(request, 'dashboard/dashboard.html', context)