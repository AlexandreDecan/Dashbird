from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^display/', include('dashboard.urls')),
    url(r'^', include(admin.site.urls)),
)
