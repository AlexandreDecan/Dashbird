from django.conf.urls import patterns, include, url
from views import DisplayView, DashboardView

urlpatterns = patterns('',
    url(r'^display/(?P<display_identifier>[\w\.+\-_]+)',
        DisplayView.as_view(),
        name='display'),
    url(r'^dashboard/(?P<dashboard_id>[0-9]+)',
        DashboardView.as_view(),
        name='dashboard'),
)
