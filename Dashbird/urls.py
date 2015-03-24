from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.core.urlresolvers import reverse_lazy
from django.views.generic.base import RedirectView

urlpatterns = patterns('',
    url(r'^gradmin/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', RedirectView.as_view(url=reverse_lazy('admin:index')), name='index'),
    url(r'^', include('dashboard.urls')),
)
