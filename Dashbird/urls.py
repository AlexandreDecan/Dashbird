from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^gradmin/', include('grappelli.urls')),
    url(r'^display/', include('dashboard.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
