from django.conf.urls import patterns, include, url
from views import DisplayView

urlpatterns = patterns('',
    url(r'^(?P<display_identifier>[\w\.+\-_]+)',
        DisplayView.as_view(),
        name='display'),
)
