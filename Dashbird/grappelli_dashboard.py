# coding=utf-8
"""
This file was generated with the customdashboard management command and
contains the class for the main dashboard.

To activate your index dashboard add the following to your settings.py::
    GRAPPELLI_INDEX_DASHBOARD = 'Dashbird.dashboard.CustomIndexDashboard'
"""

from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from grappelli.dashboard import modules, Dashboard
from grappelli.dashboard.utils import get_admin_site_name


class CustomIndexDashboard(Dashboard):
    """
    Custom index dashboard for www.
    """
    
    def init_with_context(self, context):
        site_name = get_admin_site_name(context)

        self.children.append(modules.AppList(
            title='Configuration des widgets',
            column=1,
            models=('widgets.*',)
        ))

        self.children.append(modules.AppList(
            title='Configuration de l\'affichage',
            column=1,
            models=('dashboard.*',)
        ))
        self.children.append(modules.AppList(
            title='Configuration de l\'administration',
            column=1,
            models=('django.contrib.*',)
        ))

        self.children.append(modules.LinkList(
            _('Liens'),
            column=2,
            children=[
                {
                    'title': 'Dashbird',
                    'url': 'http://www.github.com/AlexandreDecan/Dashbird/',
                    'external': True,
                    'description': 'Version de développement de Dashbird.',
                },
                {
                    'title': 'InfiniteLoop',
                    'url': 'http://www.infiniteloop.be',
                    'external': True,
                },
                {
                    'title': 'Contact',
                    'url': 'mailto:alexandre.decan@infiniteloop.be',
                    'external': True,
                },
            ]
        ))

        self.children.append(modules.RecentActions(
            _('Recent Actions'),
            limit=10,
            collapsible=False,
            column=3,
        ))


