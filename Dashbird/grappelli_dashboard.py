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
from dashboard.models import Cell, Display
from dashboard.models import Dashboard as DashboardModel


class CellList(modules.DashboardModule):
    title = 'Accès rapide'
    template = 'grp_cell_list.html'

    def init_with_context(self, context):

        for dashboard in DashboardModel.objects.order_by('name'):
            bloc = {'name': dashboard.name,
                    'url': reverse('admin:dashboard_dashboard_change', args=(dashboard.id,)),
                    'view': dashboard.get_absolute_url(),
                    'instances': []}
            for cell in Cell.objects.filter(dashboard=dashboard):
                url = 'admin:{app_label}_{model}_change'.format(app_label=cell.content_type.app_label,
                                                                model=cell.content_type.model)
                bloc['instances'].append({'name': cell.widget.name,
                                          'url': reverse(url, args=(cell.object_id,))})
            self.children.append(bloc)

        self._initialized = True


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

        self.children.append(CellList(
            column=2
        ))

        self.children.append(modules.LinkList(
            title=_('Liens'),
            column=3,
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
            limit=8,
            collapsible=False,
            column=3,
        ))


